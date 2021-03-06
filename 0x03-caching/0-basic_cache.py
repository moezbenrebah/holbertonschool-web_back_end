#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key or key in self.cache_data:
            return self.cache_data.get(key)
        return None
