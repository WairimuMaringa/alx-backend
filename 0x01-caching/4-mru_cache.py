#!/usr/bin/env python3
"""
Class that inherits from basecaching and
is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Inherits and stores. """
    def __init__(self):
        """ initialise instance. """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """ adds to cache. """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """ obtain item. """
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
