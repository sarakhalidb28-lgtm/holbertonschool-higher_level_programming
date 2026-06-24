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
        Initializes the circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the calculated area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the calculated perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with a given width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the calculated area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the calculated perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape object.
    Relies entirely on duck typing without using isinstance checks.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
