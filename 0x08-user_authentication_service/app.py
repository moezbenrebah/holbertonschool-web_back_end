#!/usr/bin/env python3
"""route module for API"""

from auth import Auth
from flask import Flask, abort, jsonify, make_response, request,
redirect, url_for


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
    session_ID = AUTH.get_user_from_session_id(session_id=session_id)
    if session_ID:
        AUTH.destroy_session(session_ID)
        return redirect(url_for('/'))

    status_code = flask.Response(status=403)
    return status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
