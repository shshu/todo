from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)

from models import task, user


@app.route("/")
def home():
    return "Hello World!"

