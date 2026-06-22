#!/usr/bin/python3
"""Defines an inheritance checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: The object to inspect.
        a_class: The base class to match against.

    Returns:
        True if obj is an instance of a subclass of a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
