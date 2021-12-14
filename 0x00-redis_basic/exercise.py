#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Union


class Cache():
    """ store an instance of the Redis client as a private variable
    named _redis (using redis.Redis()) and flush the instance
    using flushdb. """

    def __init__(self):
        """ initiate  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """ store date to database """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key