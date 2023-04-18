#!/usr/bin/env python3
"""
Class that inherits from basecaching and is
a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits and stores info. """

    def __init__(self):
        """ initialise an instance."""
        super().__init__()

    def put(self, key, item):
        """ add item to cache. """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ obtain item from cache. """
        if not key or not self.cache_data.get(key):
            return None
        return self.cache_data.get(key)
