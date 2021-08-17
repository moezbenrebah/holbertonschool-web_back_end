#!/usr/bin/env python3
"""route module for API"""

from auth import Auth
from flask import Flask, abort, jsonify, make_response, request, redirect


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """implements the POST /users route."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        check_user = AUTH.register_user(email, password)
        if check_user:
            return jsonify({"email": email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """create a new session for the user, store it the session ID as a cookie
    with key "session_id" on the response and return a JSON payload
    """
    email = request.form.get('email')
    password = request.form.get('password')

    valid_cred = AUTH.valid_login(email=email, password=password)
    if valid_cred:
        session_ID = AUTH.create_session(email)
        response = make_response({"email": "email",
                                  "message": "logged in"})
        response.set_cookie("session_id", session_ID)
        return response
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Find the user with the requested session ID. If the user exists
    destroy the session and redirect the user to GET /.
    If the user does not exist, respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id")
    user_session = AUTH.get_user_from_session_id(session_id)
    if user_session:
        AUTH.destroy_session(user_session.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """respond with 200 status code if the user exist,
    otherwise return 403 HTTP status"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """If email not registered the response will be 403 status
    otherwise, generate a token with 200 response.
    """
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        res_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": user.email, "reset_token": res_token}), 200

    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Update the password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        user = AUTH.valid_login(email=email, password=new_password)
        if reset_token:
            return jsonify({"email": user.email,
                            "message": "Password updated"}), 200

    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
