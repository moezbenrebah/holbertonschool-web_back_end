#!/usr/bin/env python3
"""lifo_cache module"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""
    def __init__(self):
        """Initializing"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)


    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            removedItem = list(self.cache_data.popitem(last=False))[0]
            print("DISCARD:", removedItem)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if not key or key not in self.cache_data:
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
