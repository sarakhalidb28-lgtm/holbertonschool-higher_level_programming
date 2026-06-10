#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
The module provides one function, lazy_matrix_mul(m_a, m_b).
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a: The first matrix (list of lists of integers/floats).
        m_b: The second matrix (list of lists of integers/floats).

    Raises:
        ValueError: If an operand is a scalar or shapes are misaligned.
        TypeError: If an operand contains invalid data types.

    Returns:
        The matrix product of m_a and m_b as a NumPy array.
    """
    # Explicitly check for scalar values (like int, float, str)
    if isinstance(m_a, (int, float, str)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if isinstance(m_b, (int, float, str)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # Let NumPy handle all other checks natively ([[]], shape mismatches, strings inside lists)
    return np.matmul(m_a, m_b)
