#!/usr/bin/env python3
"""
Creating a Cache class in Redis
"""
import redis
from uuid import uuid4
from typing import Union, Callable

class Cache:
    """
    Cache cls
    """
    def __init__(self, host='localhost', port=6379):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ki = str(uuid4())
        self._redis.set(ki, data)
        return ki 
    

    def get(self, key: str, fn: Callable=None) -> str:
        if fn is not None:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)













































































































































































        
