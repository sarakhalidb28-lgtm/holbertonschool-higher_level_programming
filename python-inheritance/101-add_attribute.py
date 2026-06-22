#!/usr/bin/python3
"""Defines a function that dynamically adds attributes to objects."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to receive the attribute.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
