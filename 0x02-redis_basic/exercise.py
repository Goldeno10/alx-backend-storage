#!/usr/bin/env python3
"""
Task:
    Create a Cache class. In the __init__ method, store an instance
     of the Redis client as a private variable named _redis
     (using redis.Redis()) and flush the instance using flushdb.

    Create a store method that takes a data argument and returns a
     string. The method should generate a random key (e.g. using uuid),
     store the input data in Redis using the random key and return the key.

    Type-annotate store correctly. Remember that data can be a str,
     bytes, int or float.
    ===================================
    The following code should not raise:

    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
    ============================================
"""


import redis
from typing import Union
import uuid


class Cache:
    """
    This class implements the caching procedure
    """
    def __init__(self):
        """This method Initializes this object"""
        _redis = redis.Redis()
        _redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates and return a random key using the uuid module"""
        key = uuid.uuid4()
        self._redis.set(key)
        return key

    def get(self, key, fn=None):
        """
        method that take a key string argument and an optional Callable
        argument named fn. This callable will be used to convert the data
        back to the desired format.
        """
        data = self._redis.get(key) if not fn else fn(self._redis.get(key))
        return data
