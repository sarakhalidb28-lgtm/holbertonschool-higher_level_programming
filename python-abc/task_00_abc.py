#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses to return
        the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
