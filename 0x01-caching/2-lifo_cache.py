#!/usr/bin/env python3
"""
Class that inherits from basecaching and is
a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ inherits and stores. """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ add item to cache. """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_key)
            print('DISCARD:', self.last_key)
        if key:
            self.last_key = key

    def get(self, key):
        """ obtain item from cache. """
        return self.cache_data.get(key)
