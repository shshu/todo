from flask import Blueprint, jsonify, request

# from models.user import User

login_api = simple_page = Blueprint('login_api', __name__, template_folder='templates')
@login_api.route('/api/login', methods=['POST'])
def login():
    """
    Authenticate user and return token
    """
    data = request.get_json()
    import pdb;pdb.set_trace()
    if not data:
        return jsonify(msg="expected dict with username, password key value"), HTTPStatus.BAD_REQUEST
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        u1 = User.query().all().filter_by(username=username).all()
        import pdb;pdb.set_trace()
        # TODO auth this user
        access_token = create_access_token(identity=username)
        if access_token is not None:
            print('access token: ' + access_token)
            return jsonify(access_token=access_token)
        else:
            abort(403)
    else:
        abort(400)
