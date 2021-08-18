#!/usr/bin/env python3
"""main module"""

import requests as req
import json


def register_user(email: str, password: str) -> None:
    """register user credentials"""
    data = {"email": EMAIL, "password": PASSWD}
    user = req.post('http://localhost:5000/users', data=data)
    assert user.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """test log in with wrong password"""
    data = {"email": EMAIL, "password": PASSWD}
    user = req.post('http://localhost:5000/sessions', data=data)
    assert user.status_code == 401


def log_in(email: str, password: str) -> str:
    """test log in with valid credentials"""
    data = {"email": EMAIL, "password": PASSWD}
    user = req.post('http://localhost:5000/sessions', data=data)
    assert user.status_code == 200
    return user.cookies.get("session_id")


def profile_unlogged() -> None:
    """test if the user doesn't exist"""
    user = req.get('http://localhost:5000/profile')
    assert user.status_code == 403


def profile_logged(session_id: str) -> None:
    """test if the user exist"""
    session = log_in(EMAIL, PASSWD)
    cookies = {"session_id": session}
    user = req.get('http://localhost:5000/profile', params=cookies)
    assert user.status_code == 200


def log_out(session_id: str) -> None:
    """test user log out properly"""
    session = log_in(EMAIL, PASSWD)
    cookies = {"session_id": session}
    user = req.delete('http://localhost:5000/sessions', params=cookies)
    assert user.status_code == 200


def reset_password_token(email: str) -> str:
    """test reset password end point"""
    data = {"email": EMAIL}
    user = req.post('http://localhost:5000/reset_password', data=data)
    assert user.status_code == 200
    data = json.loads(user.content)
    return data.get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """test updating password query"""
    data = {"email": EMAIL,
            "reset_token": reset_token,
            "new_password": NEW_PASSWD}
    user = req.put('http://localhost:5000/reset_password', data=data)
    assert user.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
