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
    Simple `FIFO` caching algorithm implementation.

    Inherits from `BaseCaching`.\n
    Defines two methods:
        * `put` - For adding items to the cache using `FIFO` algorithm
        * `get` - For retrieving items from the cache
    """

    def put(self, key, item):
        """
        Method for adding items to cache following `FIFO` algorithm.

        First, validate that `key` and `item` passed are not Null. Check if
        key exists in cache - if yes, replace its value with `item`. If not,
        and max number of items in cache is reached, remove the oldest item
        in cache then add the new item.

        Parameters
        ----------
        key : Any
            Identifies cache items
        item : Any
            The cache item
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
        Retrieves items from cache.

        First, ensure `key` is not null and it exists in the cache keys.
        Then, get the item associated with the key in cache.

        Parameters
        ----------
        key : Any
            Identifies items in cache

        Returns
        -------
        item : Any
            Item in cache associated with key
        """

        if key is None:
            return None
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
