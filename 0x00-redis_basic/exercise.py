#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Callable, Union


class Cache():
    """ store an instance of the Redis client as a private variable
    named _redis (using redis.Redis()) and flush the instance
    using flushdb. """

    def __init__(self):
        """ initiate  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store date to database """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str,
                                                          bytes, int, float]:
        """ get function """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ convert back to string """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ convert back to int """
        data = self._redis.get(key)
        return int(data.decode("utf-8"))
