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


def call_history(method: Callable) -> Callable:
    """store inputs and outputs parameters"""
    @functools.wraps(method)
    def wrapper_input(self, *args, **kwargs):
        """appending inputs and outputs to create keys list"""
        wrapper_method = method.__qualname__
        data = str(args)
        result = method(self, data)
        self._redis.rpush(f'{wrapper_method}:inputs', data)
        self._redis.rpush(f'{wrapper_method}:outputs', result)
        return result
    return wrapper_input


class Cache:
    """cache class"""

    def __init__(self):
        """initialization"""

        self._redis = redis.Redis()
        self._redis.flushdb

    @call_history
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
