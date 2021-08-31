#!/usr/bin/env python3
"""redis-py module"""

import functools
from typing import Callable, Optional, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """counts the cache methods' calls number"""
    @functools.wraps(method)
    def wrapper_count_calls(self, *args, **kwargs):
        """increment the count of key whenever the method is called
        and return the value
        """
        wrapper_count_calls.count = 0
        wrapper_method = method.__qualname__
        self._redis.incr(wrapper_method)
        return method(self, *args, **kwargs)
    return wrapper_count_calls


class Cache:
    """cache class"""

    def __init__(self):
        """initialization"""

        self._redis = redis.Redis()
        self._redis.flushdb

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key and store value of that key"""

        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None):
        """return back the data value in desirable format"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key):
        """return key value as a string"""
        return get(key, str)

    def get_int(self, key):
        """return key value as an integer"""
        return get(key, int)
