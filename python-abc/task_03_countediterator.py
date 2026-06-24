#!/usr/bin/env python3
"""
This module defines the CountedIterator class.
It wraps an iterator to keep track of the number of items fetched.
"""


class CountedIterator:
    """
    An iterator wrapper that maintains a count of iterated items.
    """

    def __init__(self, some_iterable):
        """
        Initializes the iterator object and the counter tracker.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.counter

    def __iter__(self):
        """
        Returns the iterator instance itself.
        """
        return self

    def __next__(self):
        """
        Increments the counter and fetches the next item.
        Raises StopIteration when no items are left.
        """
        # Fetch item first; if empty, StopIteration is raised before incrementing
        item = next(self.iterator)
        self.counter += 1
        return item
