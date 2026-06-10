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
        m_a: The first matrix (list of lists or array-like).
        m_b: The second matrix (list of lists or array-like).

    Returns:
        The matrix product of m_a and m_b as a NumPy array or nested list.
    """
    return np.matmul(m_a, m_b)
