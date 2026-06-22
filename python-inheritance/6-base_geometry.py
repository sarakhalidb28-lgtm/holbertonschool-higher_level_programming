#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Computes the area of the geometry.

        Raises:
            Exception: Always, because the method is not implemented.
        """
        raise Exception("area() is not implemented")
