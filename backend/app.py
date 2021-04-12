import logging
from http import HTTPStatus

from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object('config.Config')
jwt = JWTManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from api import login, todo
# from models.task import Task
from models import task, user


# get_jwt_identity()
@app.route("/")
@jwt_required()
def home():
    username = get_jwt_identity()
    return f"Hello World! {username}"

@app.route("/api/test")
def test():
    return f"alive!"

# export FLASK_APP=backend/app.py
# export FLASK_ENV=development
# flask run
# curl -X GET localhost:5000/ -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNzczOTI1OSwianRpIjoiYWIxY2QzNWEtNTk5MS00MjdiLThkYTItOTAwZGE1NGNkMjkwIiwibmJmIjoxNjE3NzM5MjU5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiYWRtaW4iLCJleHAiOjE2MTc3NDAxNTl9.KEPXFvgGVX_ouZYYRK2G8KOmHyFlGPedh9TD-0uk35Y"


# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(
#         render_template("404.html"),
#         404
#      )
