#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The module provides one function, say_my_name(first_name, last_name="").
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name: The first name string.
        last_name: The last name string (defaults to empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
