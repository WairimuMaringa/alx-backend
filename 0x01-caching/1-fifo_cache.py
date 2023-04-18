#!/usr/bin/python3
"""
class that inherits from basecaching and is
a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ inherits and stores. """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            drop_key = sorted(self.cache_data)[0]
            self.cache_data.pop(drop_key)
            print('DISCARD: {}'.format(drop_key))

    def get(self, key):
        return self.cache_data.get(key)
