from flask import Flask
from Project import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Cyber Savvy Ninjas!</p>"

@app.route("/therapist")
def therapy():
    res = therapist("happy")
    return "<h1>" + res + "</h1>"