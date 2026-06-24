#!/usr/bin/env python3
"""Module for shapes and duck typing"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract shape class"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        raise NotImplementedError


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of circle"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
