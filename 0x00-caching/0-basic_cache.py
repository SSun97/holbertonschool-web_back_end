#!/usr/bin/env python3
""" Create a class BasicCache that inherits from BaseCaching
and is a caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Doc """

    def put(self, key, item):
        """ Add an item in the cache """
        self.cache_data[key] = item
        # raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        if key is None or key is '' or key not in self.cache_data:
            return None
            # raise NotImplementedError(
            #     "get must be implemented in your cache class")
        return self.cache_data[key]
