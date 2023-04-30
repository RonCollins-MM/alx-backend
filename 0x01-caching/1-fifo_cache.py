#!/usr/bin/env python3

"""
Simple implementation of FIFO caching algorithm.

Classes defined:
---------------

`FIFOCache`
    - Inherits from `Basecaching`.
    - Defines two methods: `put` and `get`
"""

from base_cahing import BaseCaching

class FIFOCache(BaseCaching):
    """

    """

    def put(self, key, item):
        """

        """

        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item_key = next(iter(self.cache_data))
            print(f'DISCARD: {first_item_key}')
            del self.cache_data[first_item_key]
        self.cache_data.update({key: item})

    def get(self, key):
        """

        """

        if key is None:
            return None
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
