import json
import redis

redis_cache = redis.Redis(host='localhost', port=6379, db=0)


class RedisFunction:

    @staticmethod
    def get_key(key):
        return redis_cache.get(key)

    @staticmethod
    def set_key(key, cache_data):
        return redis_cache.set(key, cache_data)


