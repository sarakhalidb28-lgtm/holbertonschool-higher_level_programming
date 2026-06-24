#!/usr/bin/env python3
"""
This module defines the Shape abstract base class, its concrete subclasses
Circle and Rectangle, and a standalone function to process them using duck typing.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle shape.
    """

    def __init__(self, radius):
        """
        Initializes the circle with a given radius and validates it.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be greater than 0")
        self.__radius = radius

    @property
    def radius(self):
        """Getter for radius."""
        return self.__radius

    def area(self):
        """
        Returns the calculated area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Returns the calculated perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with a given width and height and validates them.
        """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if width <= 0:
            raise ValueError("width must be greater than 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if height <= 0:
            raise ValueError("height must be greater than 0")
            
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    def area(self):
        """
        Returns the calculated area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the calculated perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape object.
    Relies entirely on duck typing without using isinstance checks.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
