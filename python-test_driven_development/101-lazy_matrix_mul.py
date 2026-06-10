#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """

    if isinstance(m_a, (int, float, str)) or isinstance(m_b, (int, float, str)):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    return np.array(m_a) @ np.array(m_b)
