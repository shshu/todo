import json
import logging
from http import HTTPStatus

from flask import Flask, render_template, request
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


class Encoder(json.JSONEncoder):
    def default(self, obj):
    
        if isinstance(obj, task.Task):
            return { 'id': obj.id,'user_id' : obj.user_id,  'task' : obj.task,  'is_done': obj.is_done, 'severity': obj.severity.value}

        if isinstance(obj, user.User):
            return { 'id': obj.id,'username' : obj.username,  'email' : obj.email}
    
        return json.JSONEncoder.default(self, obj) # default


app.json_encoder = Encoder

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/api/healthcheck")
def test():
    return "alive"

