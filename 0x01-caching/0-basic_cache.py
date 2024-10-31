#!/usr/bin/env python3
"""a class BasicCache that inherits from BaseCaching
 and is a caching system:
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A Basic caching system inherits
    from base caching
    """
    def __init__(self):
        """Initialize"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item
        value for the key key. If key or item is None,
        this method should not do anything
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
