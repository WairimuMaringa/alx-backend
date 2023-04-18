#!/usr/bin/python3
"""
Class that inherits from basecaching and is
a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits and stores info. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
