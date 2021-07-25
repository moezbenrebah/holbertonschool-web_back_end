#!/usr/bin/env python3
"""Mru_cache module"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        """Initializing"""
        super().__init__()
        self.cache_data = OrderedDict()

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
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
