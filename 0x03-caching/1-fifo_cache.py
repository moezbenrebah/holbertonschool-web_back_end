#!/usr/bin/env python3
"""fifo_cache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""
    def __init__(self):
        """Initializing"""
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removedItem = list(self.cache_data.keys())[0]
            print("DISCARD:", removedItem)
            self.cache_data.pop(removedItem)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key or key in self.cache_data:
            return self.cache_data.get(key)
        return None
