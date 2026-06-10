#!/usr/bin/python3
"""
This is the "4-print_square" module.
The module provides one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer).

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is less than 0.
    """
    # If size is a float and is less than 0, it must raise a TypeError
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    # General type verification (strictly allowing only ints, excluding bools)
    if type(size) is not int:
        raise TypeError("size must be an integer")

    # Value range verification
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square pattern
    for _ in range(size):
        print("#" * size)
