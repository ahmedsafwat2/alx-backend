#!/usr/bin/env python3
'''
Task 1: FIFO Caching
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    A class `FIFOCache` that inherits from `BaseCaching`
    and is a caching system
    '''
    def __init__(self):
        """
        __init__
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and (self.cache_data.get(key, None) is None):
            iter_dict = iter(self.cache_data)
            first_element = next(iter_dict)
            self.cache_data.pop(first_element)
            print(f"DISCARD: {first_element}")
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
