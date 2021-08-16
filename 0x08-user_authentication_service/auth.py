#!/usr/bin/env python3
"""hash password module"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """returns byte string"""

    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return uuid.uuid4()


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """initialize"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """returns a User object"""
        try:
            checked_email = self._db.find_user_by(email=email)
            if checked_email:
                raise ValueError
                print(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """locating the user by email. If it exists,
        check the password with 'bcrypt.checkpw'
        """
        try:
            located_user_email = self._db.find_user_by(email=email)
            valid_user = bcrypt.checkpw(password.encode('utf-8'),
                                        located_user_email.hashed_password)
            if valid_user:
                return True
            return False

        except NoResultFound:
            return False