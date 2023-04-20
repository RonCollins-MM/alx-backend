#!/usr/bin/python3
""" BasicCache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class that implements a simple caching system
    """

    def put(self, key, item):
        """
        Adds the key and item(value) passed to a dictionary that acts as a
        local cache.
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieves the item(value) associated with the key in the cache
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
