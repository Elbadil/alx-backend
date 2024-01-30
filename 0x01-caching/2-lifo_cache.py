#!/usr/bin/env python3
"""Defining a class LIFOCache"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """Initializes a new LIFOCache instance"""
        super().__init__()
        self.last_updated_key = None

    def put(self, key, item):
        """Adds an item to the cache_data dictionary
        and removes the last added or updated item if the length
        the dictionary is higher than MAX_ITEMS"""
        if key is None and item is None:
            return

        last_item_key = ""
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_updated_key:
                last_item_key = self.last_updated_key
                self.last_updated_key = None
            else:
                last_item_key = list(self.cache_data.keys())[-2]
            del self.cache_data[last_item_key]
            print(f'DISCARD: {last_item_key}')
        else:
            self.last_updated_key = key

    def get(self, key):
        """returns the value of a key if the key exists"""
        value = self.cache_data.get(key)
        if not value or key is None:
            return None
        return value
