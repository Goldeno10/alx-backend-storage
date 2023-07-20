#!/usr/bin/env python3
"""
Task:
    In this tasks, we will implement a get_page
    function (prototype: def get_page(url: str) -> str:). The core of
    the function is very simple. It uses the requests module to obtain
    the HTML content of a particular URL and returns it.

    Start in a new file named web.py and do not reuse the code written
    in exercise.py.
    Inside get_page track how many times a particular URL was accessed
    in the key "count:{url}" and cache the result with an expiration
    time of 10 seconds.
Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow
  response and test your caching.
Bonus: implement this use case with decorators.
"""


import functools
import requests
import redis
import time
from typing import Callable


# Redis connection
redis_client = redis.Redis()


# Helper function to generate a cache key
def get_cache_key(url: str) -> str:
    return f"cache:{url}"


# Helper function to generate a count key
def get_count_key(url: str) -> str:
    return f"count:{url}"


# Decorator for caching with expiration time
def cache_with_expiration(seconds: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(url: str) -> str:
            cache_key = get_cache_key(url)
            cached_result = redis_client.get(cache_key)
            if cached_result:
                return cached_result.decode('utf-8')

            result = func(url)
            redis_client.setex(cache_key, seconds, result)
            return result

        return wrapper
    return decorator


# Decorator for tracking access count
def track_access_count(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(url: str) -> str:
        count_key = get_count_key(url)
        redis_client.incr(count_key)
        return func(url)

    return wrapper


@cache_with_expiration(seconds=10)
@track_access_count
def get_page(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return f"Error: Unable to fetch the page for URL - {url}"
