#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in Python list
to provide verbose console notifications when elements are added or removed.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications to stdout
    whenever elements are appended, extended, removed, or popped.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a success notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Extends the list with an iterable and prints a notification with the count.
        """
        count = len(x)
        super().extend(x)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Removes the first occurrence of an item from the list.
        Prints a notification before removal.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns an item at the given index (default last item).
        Prints a notification before popping.
        """
        # Resolve index to find the actual item about to be popped
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
