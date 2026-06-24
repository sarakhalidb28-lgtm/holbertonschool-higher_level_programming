#!/usr/bin/env python3
"""
This module demonstrates the mixin design pattern in Python.
It defines SwimMixin and FlyMixin to compose features into a Dragon class.
"""


class SwimMixin:
    """
    Mixin that provides swimming capability.
    """

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying capability.
    """

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon, composed of SwimMixin and FlyMixin capabilities.
    """

    def roar(self):
        """Prints the unique roaring capability of a dragon."""
        print("The dragon roars!")
