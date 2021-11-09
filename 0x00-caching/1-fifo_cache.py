#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from BaseCaching
and is a caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        # self.cache_data = {}
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        self.cache_data[key] = item
        if key not in self.key_list:
            self.key_list.append(key)
        if len(self.key_list) > self.MAX_ITEMS:
            print("DISCARD: " + self.key_list[0])
            del self.cache_data[self.key_list[0]]
            del self.key_list[0]
        # raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        if key is None or key is '' or key not in self.cache_data:
            return None
            # raise NotImplementedError(
            #     "get must be implemented in your cache class")
        return self.cache_data[key]
