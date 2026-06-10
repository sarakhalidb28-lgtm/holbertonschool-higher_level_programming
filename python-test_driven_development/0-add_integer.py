#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module provides one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, defaults to 98).

    Raises:
        TypeError: If a or b is not an integer, float, or is NaN/Inf.

    Returns:
        The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # التحقق من قيم NaN (أي قيمة لا تساوي نفسها هي NaN في بايثون)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # التحقق من قيم Infinity
    if a in [float('inf'), float('-inf')]:
        raise TypeError("a must be an integer")
    if b in [float('inf'), float('-inf')]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
