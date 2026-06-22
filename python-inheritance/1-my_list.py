#!/usr/bin/python3
"""This module defines a custom list class that inherits from standard list."""


class MyList(list):
    """A custom list subclass with specialized sorting print behavior."""

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        print(sorted(self))
