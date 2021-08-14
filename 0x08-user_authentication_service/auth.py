#!/usr/bin/env python3
"""hash password module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """returns byte string"""

    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    return hashed
