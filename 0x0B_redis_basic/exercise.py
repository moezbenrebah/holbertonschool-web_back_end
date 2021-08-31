#!/usr/bin/env python3
"""redis-py module"""

from typing import Callable, Union
import redis
import uuid


class Cache:
    """cache class"""

    def __init__(self):
        """initialization"""

        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key and store value of that key"""

        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            **fn: Callable) -> Union[str, bytes, int, float]:
        """return the value of key"""

        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key):
        """return key value as a string"""

        return get(key, str)

    def get_int(self, key):
        """return key value as an integer"""

        return get(key, int)
