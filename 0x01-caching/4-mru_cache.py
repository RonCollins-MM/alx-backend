#!/usr/bin/env python3

"""
Implementation of a simple MRU(Most Recently Used) caching algorithm.

Defines one class:
    * `MRUCache`
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Implements a simple `MRU` caching algorithm.

    Contains 4 methods:
        * `get` - Fetches the next item in the cache
        * `put` - Adds an item to the cache
        * `update_age_bit_table` (private) - Modifies the age-bit table
            which is used to track usage of cache items
        * `get_MRU_item` (private) - Returns the key of the most recently
        used cache item
    """

    def __init__(self):
        """
        Initialize a MRUCacing object with the necessary attributes (see below)
        """

        super().__init__()
        """Initialises the cache store using the parent class constructor"""

        self.__age_bit_table = {}
        """Will keep track of cache item usage using `age_bit` int value.

        Has a mapping of:
            `{ 'key' : age_bit }`
        (See doc string for `next_age_bit` below for defn of age_bit)
        """

        self.__next_age_bit = 0
        """Stores the value of the next age_bit to be used in caching.

        The age_bit is just an `int` number that is incremented every time the
        cache is accessed and assigned to the last accessed cached item in
        the `age_bit_table`.
        """

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
        self.__update_agebit_table(key)
        return self.cache_data[key]

    def put(self, key, item):
        """
        Inserts an item into the cache.

        First, ensure `key` and `item` passed are not Null. If key exists in
        cache, replace its value with `item`, and update the cache table
        accordingly. If cache is full, discard the most recently used(MRU)
        cache item. The MRU is determined by reading the `age_bit_table`. Once
        discarded, add new item to cache and update the table.

        Parameters
        ----------
        key : Any
            The key of the cache item
        item : Any
            The cache item
        """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.__update_agebit_table(key)
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            MRU_item_key = self.__get_MRU_item()
            print(f'DISCARD: {MRU_item_key}')
            del self.cache_data[MRU_item_key]
            del self.__age_bit_table[MRU_item_key]
        self.cache_data.update({key: item})
        self.__update_agebit_table(key)

    def __update_agebit_table(self, key):
        """
        Private method to update `age_bit_table`.

        Whenever any cache item is accessed in any way (new item or update),
        an `age_bit` `int` is assigned to it and both values stored in the
        `age_bit_table`.

        Parameters
        ----------
        key : Any
            The key to be used in updating the table
        """

        if key in self.__age_bit_table.keys():
            self.__age_bit_table[key] = self.__next_age_bit
            self.__next_age_bit += 1
            return
        else:
            self.__age_bit_table.update({key: self.__next_age_bit})
            self.__next_age_bit += 1

    def __get_MRU_item(self):
        """
        Returns the key of the LRU cache item.

        First finds the smallest `age_bit` from the table and then returns the
        key associated with it.
        This function is utilised whenever a cache item needs to be deleted
        when the cache is full.
        """

        keys = self.__age_bit_table.keys()
        items = self.__age_bit_table.values()
        smallest_agebit = sorted(items, reverse=True)[0]
        index = list(items).index(smallest_agebit)

        return list(keys)[index]
