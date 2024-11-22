#!/usr/bin/env python3
""" setup flask web server"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
AUTH = Auth()


@app.route('/', methods=["GET"])
def hello():
    """return json string"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"])
def users():
    """
    signing up user
    """
    # extract email and password
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, " message": "user created"}), 201
    except ValueError as err:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ for user login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if (AUTH.valid_login(email, password)):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify(
            {"email": email,
             "message": "logged in"
             }), 200)
        response.set_cookie("session_id", session_id)
        return response
    else:
        return abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    response = redirect('/')
    response.delete_cookie('session_id')
    return response


@app.route('/profile', methods=["GET"])
def profile():
    session_id = request.cookies.get('session_id')
    logging.debug(f"Session ID from cookie: {session_id}")
    if not session_id:
        logging.debug("session_id is not gotten")
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        logging.debug("No user found with the provided session ID.")
        abort(403)
    logging.debug(f"User found: {user.email}")
    return jsonify({"email": user.email}), 200

@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """route for reset password"""
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token})
    except ValueError:
        abort(403)

@app.route('/reset_password', methods=['PUT'])
def get_reset_password_token():
    """route for update password"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
