#!/usr/bin/python3
"""Defines a base geometry class with validation checks."""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Computes the area of the geometry.

        Raises:
            Exception: Always, because the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given parameter is a positive integer.

        Args:
            name (str): The descriptive name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not exactly an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
