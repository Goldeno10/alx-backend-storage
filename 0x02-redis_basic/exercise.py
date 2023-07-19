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
