
from flask import Flask, jsonify, request
from main import compile_server

# export FLASK_APP = server.py
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/compile", methods=["POST"])
def compile_program():
    code = request.json['code']
    return jsonify(compile_server(code))

