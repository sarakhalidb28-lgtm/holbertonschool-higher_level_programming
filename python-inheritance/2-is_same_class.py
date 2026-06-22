#!/usr/bin/python3
"""Defines a function to check exact object class membership."""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a specified class.

    Args:
        obj: The object to inspect.
        a_class: The exact class to match against.

    Returns:
        True if obj is exactly an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
