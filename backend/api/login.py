from http import HTTPStatus

from app import app, bcrypt, db
from flask import abort, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User
from sqlalchemy.exc import SQLAlchemyError


def get_user(username):
    user = User.query.filter_by(username=username).all()
    if user:
        return user[0]
    return None

def is_authenticate(username, password):
    """
    Authenticate a username/password - this sample routine simply checks
    the username/password against a hard-coded table, a real-world
    implementation would authenticate users against a database or external
    service.
    """
    user = User.query.filter_by(username=username).all()
    if not user:
        return False
    
    # TODO save the admin with the == bcrypt.generate_password_hash(password): bcrypt.check_password_hash(pw_hash, 'secret')
    if user[0].password:
        return True

    return False


@app.route('/api/login', methods=['POST'])
def login():
    """
    Authenticate user and return token
    """
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        # User.query.filter_by(username='admin').all()
        if is_authenticate(username, password):
            access_token = create_access_token(identity=username)
            app.logger.info(f'created new token {access_token} for user {username}')
            return jsonify(access_token=access_token)
        else:
            app.logger.info(f'cloud not authenticate {username}')
            abort(403)
    else:
        abort(400)


@app.route('/api/sign_up', methods=['POST'])
def sign_up():
    """
    Sing up new User
    """
    data = request.get_json()
    if 'username' in data and 'password' in data and 'email' in data:
        username = data['username']
        password = data['password']
        email = data['email']
        if get_user(username):
            app.logger.info(f'try to create user that already exist {username} {email}')
            return jsonify(error='User aleady exist'), HTTPStatus.BAD_REQUEST
        try:
            usr = User(username, password, email)
            db.session.add(usr)
            db.session.commit()
            app.logger.info(f'created new user {username} {email}')
            return jsonify(msg=f'new user has been created {username}'), HTTPStatus.CREATED
        except SQLAlchemyError as e:
            app.logger.error(e)
            return jsonify(error=f'DB error could not create '), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        abort(HTTPStatus.BAD_REQUEST)

@app.route("/api/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
