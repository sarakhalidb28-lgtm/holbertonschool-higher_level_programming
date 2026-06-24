#!/usr/bin/env python3
"""Module for shapes and duck typing"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class for shapes"""

    @abstractmethod
    def area(self):
        """Return area"""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return perimeter"""
        raise NotImplementedError


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize circle"""
        self.radius = radius

    def area(self):
        """Return circle area"""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
