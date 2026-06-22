#!/usr/bin/python3
"""This module defines a custom integer class named MyInt.

The MyInt class inherits from the built-in int class but has its
equality (==) and inequality (!=) operators inverted.
"""


class MyInt(int):
    """A rebel integer class that has == and != operators inverted."""

    def __eq__(self, other):
        """Overrides equality to return inequality behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides inequality to return equality behavior."""
        return super().__eq__(other)
