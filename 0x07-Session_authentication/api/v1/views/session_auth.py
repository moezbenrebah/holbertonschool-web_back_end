#!/usr/bin/env python3
"""session route"""

from models.user import User
from flask import abort, jsonify, request
from api.v1.views import app_views
import os
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def parse_request() -> str:
    """create a route POST /auth_session/login"""
    email = request.form.get('email')
    if not email or email is None:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password or password is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_value = auth.create_session(objs[0].id)
    result = jsonify(objs[0].to_json())
    session_key = os.getenv("SESSION_NAME")
    result.set_cookie(session_key, session_value)
    return result


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_auth_logout() -> str:
    """destroy /auth_session/logout"""
    from api.v1.app import auth

    if auth.destroy_session(request) is False:
        abort(404)

    return jsonify({}), 200
