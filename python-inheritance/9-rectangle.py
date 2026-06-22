#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle shape using BaseGeometry validation."""

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle instance."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string description of the rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
