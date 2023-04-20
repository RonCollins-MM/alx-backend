#!/usr/bin/python3
""" BasicCache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class that implements a simple caching system
    """

    def put(self, key, item):
        if key is None or item is None:
            return

        self.cache_data.update({key: item})

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        
        return self.cache_data[key]
