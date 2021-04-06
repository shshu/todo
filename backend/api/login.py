from app import app, bcrypt
from flask import abort, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User


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
        import pdb;pdb.set_trace()
        # User.query.filter_by(username='admin').all()
        if is_authenticate(username, password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
        else:
            import pdb;pdb.set_trace()
            abort(403)
    else:
        abort(400)
    return 'hello login'
