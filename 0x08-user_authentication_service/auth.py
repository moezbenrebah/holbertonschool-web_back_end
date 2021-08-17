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
    return str(uuid.uuid1())


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

    def create_session(self, email: str) -> str:
        """returns the session ID as a string."""
        try:
            user = self._db.find_user_by(email=email)

            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return

    def get_user_from_session_id(self, session_id: str) -> str:
        """returns the corresponding User or None"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user

        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        """updates the corresponding user’s session ID to None"""
        if user_id is None:
            return None

        user = self._db.update_user(user_id, session_id=None)
        return user

    def get_reset_password_token(self, email: str) -> str:
        """Find the user corresponding to the email. If the user does not exist
        raise a ValueError exception. If it exists,
        generate a UUID and update the user’s reset_token database field.
        Return the token.
        """
        try:
            valid_email = self._db.find_user_by(email=email)
            token_uuid = _generate_uuid()
            self._db.update_user(valid_email.id, reset_token=token_uuid)
            return token_uuid

        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """locate a corresponding user using the reset_token
        if it doesn't exist raise ValueError otherwise,
        hash the password and update the user's hashed_password
        and reset the fields to None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                password = _hash_password(password)
                self._db.update_user(user.id, hashed_password=password,
                                     reset_token=None)

        except NoResultFound:
            raise ValueError
