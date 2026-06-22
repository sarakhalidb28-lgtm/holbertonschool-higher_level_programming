#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape using Rectangle behavior."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string description of the square instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)
