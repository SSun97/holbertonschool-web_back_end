#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count calls """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Callable:
        """ wrapped funcion """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ call history """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapped function """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


class Cache():
    """ store an instance of the Redis client as a private variable
    named _redis (using redis.Redis()) and flush the instance
    using flushdb. """

    def __init__(self):
        """ initiate  """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

def replay(method: Callable):
    """ display the history of calls of function """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(inputList, outputList))
    for a, b in redis_zipped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))