#!/usr/bin/env python3
""" setup flask web server"""
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"])
def hello():
    """return json string"""
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=["POST"])
def users():
    #extract email and password
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email":email,"message":"user created"}), 201
    except ValueError as err:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
