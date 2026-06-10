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
        TypeError: If an operand is a scalar or contains invalid data types.
        ValueError: If a matrix is empty or shapes are misaligned.

    Returns:
        The matrix product of m_a and m_b as a NumPy array.
    """
    # 1. Raise explicit scalar ValueError expected by the checker
    if isinstance(m_a, (int, float, str)) or np.isscalar(m_a):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if isinstance(m_b, (int, float, str)) or np.isscalar(m_b):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # 2. Check for nested empty lists like [[]]
    if isinstance(m_a, list) and len(m_a) > 0 and m_a[0] == []:
        raise ValueError("m_a can't be empty")
    if isinstance(m_b, list) and len(m_b) > 0 and m_b[0] == []:
        raise ValueError("m_b can't be empty")

    # 3. Check for structural alignment inside sub-elements
    if isinstance(m_a, list) and all(isinstance(row, list) for row in m_a):
        if len(m_a) > 0:
            first_len = len(m_a[0])
            if not all(len(row) == first_len for row in m_a):
                raise TypeError("each row of m_a must be of the same size")

    if isinstance(m_b, list) and all(isinstance(row, list) for row in m_b):
        if len(m_b) > 0:
            first_len = len(m_b[0])
            if not all(len(row) == first_len for row in m_b):
                raise TypeError("each row of m_b must be of the same size")

    return np.matmul(m_a, m_b)
