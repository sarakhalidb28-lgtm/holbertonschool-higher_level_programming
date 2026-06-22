#!/usr/bin/python3
"""Defines a function to check class type and inheritance relationships."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to inspect.
        a_class: The class to check against.

    Returns:
        True if obj is an instance or inherited instance; otherwise False.
    """
    return isinstance(obj, a_class)
