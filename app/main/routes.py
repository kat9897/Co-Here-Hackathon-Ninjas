from flask import jsonify, render_template, request
from .Project import therapist
from . import main


@main.route('/', methods=['GET'])
def index():

    return render_template('chat.html')


@main.route('/chat', methods=['POST'])
def chat():
    body = request.json

    res = therapist(body["content"])
    return jsonify({"content": res})