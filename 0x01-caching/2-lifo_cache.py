#!/usr/bin/env python3

"""
Simple implementation of `LIFO` caching algorithm.

Classes defined:
---------------

`LIFOCache`
    - Inherits from `Basecaching`.
    - Defines two methods: `put` and `get`
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Simple `LIFO` caching algorithm implementation.

    Inherits from `BaseCaching`.\n
    Defines two methods:
        * `put` - For adding items to the cache using `LIFO` algorithm
        * `get` - For retrieving items from the cache
    """

    def put(self, key, item):
        """
        Method for adding items to cache following `LIFO` algorithm.

        First, validate that `key` and `item` passed are not Null. Check if
        key exists in cache - if yes, replace its value with `item`
        and move it to the end of the dictionary. If not, and max number of
        items in cache is reached, remove the item last inserted into
        in cache which will be the right most item.

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
            self.cache_data[key] = self.cache_data.pop(key) # Move to the end
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            latest_item = self.cache_data.popitem() # Will remove end item
            print(f'DISCARD: {latest_item[0]}')
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
