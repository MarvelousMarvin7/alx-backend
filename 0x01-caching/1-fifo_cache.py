#!/usr/bin/env python3
"""Caching with FIFO algorithm"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache that inherits from BaseCaching
    using first in first out to remove data from the
    dictionary
    """
    def __init__(self):
        """initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns item to key and discard or del first data"""
        if key is None or item is None:
            pass

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
