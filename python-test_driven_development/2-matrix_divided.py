#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module provides one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (integer or float).

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix containing the divided elements rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(msg)

    # Validating structural row lengths against the initial nested list size
    if not all(len(row) == len(matrix) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
