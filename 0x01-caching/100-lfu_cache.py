#!/usr/bin/env python3
"""
Class that inherits from basecaching and
is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ inherits and stores. """
    def __init__(self):
        """ initialise instance. """
        super().__init__()
        self.cache_data = OrderedDict()
        self.lfu = ""

    def put(self, key, item):
        """ add item to cache. """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.lfu = key
                else:
                    discarded = self.lfu
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.lfu = key
            else:
                self.cache_data[key] = item
                self.lfu = key

    def get(self, key):
        """ obtain item. """
        if key in self.cache_data:
            self.lfu = key
            return self.cache_data[key]
