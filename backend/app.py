# from http import HTTPStatus

# from flask import Flask, request
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
# from flask_sqlalchemy import SQLAlchemy

# from api.login import login_api

# app = Flask(__name__)
# app.register_blueprint(login_api)
# app.config.from_object('config.DevConfig')
# jwt = JWTManager(app)
# app.config.from_object('config.DevConfig')
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

# from api import *

# # from models.task import Task
# # from models import user


# #pw_hash = bcrypt.generate_password_hash(app.secret_key, 10)
# #bcrypt.check_password_hash(pw_hash, 'secret') # returns True
# # get_jwt_identity()
# @app.route("/")
# # @jwt_required()
# def home():
#     #key = get_jwt_identity()
#     # from models.user import User
#     # u1 = User.query.all()
#     return "Hello World!"


# app.run()


from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

import resources
import views

import models

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

