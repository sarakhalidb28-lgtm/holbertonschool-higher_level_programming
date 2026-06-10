#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The module provides one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The input string to parse and print.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Flag to drop leading spaces at the start of a new line segment
    skip_space = True

    for char in text:
        if skip_space:
            if char == ' ':
                continue
            skip_space = False

        print(char, end="")

        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
