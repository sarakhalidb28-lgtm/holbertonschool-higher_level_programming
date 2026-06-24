#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python using Fish and Bird
parent classes to construct a FlyingFish child class.
"""


class Fish:
    """
    Class representing a fish with swim and habitat attributes.
    """

    def swim(self):
        """Prints swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird with fly and habitat attributes.
    """

    def fly(self):
        """Prints flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints the natural habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """Overrides the bird's fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the fish's swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat description for a flying fish."""
        print("The flying fish lives both in water and the sky!")
