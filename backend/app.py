from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevConfig')


@app.route("/")
def home():
    return "Hello World!"
