#!/usr/bin/env python3
'''
Task 2: LIFO Caching
'''


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    '''
    A class `FIFOCache` that inherits from `BaseCaching`
    and is a caching system
    '''
    def __init__(self):
        """
        __init__
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                self.cache_data.get(key, None) is None):
            last_item, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_item}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
