#!/usr/bin/env python3
"""Module for task 0."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key. If key is None or if the key doesn't exist in
        self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
