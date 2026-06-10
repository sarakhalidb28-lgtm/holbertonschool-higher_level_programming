#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """

    if np.isscalar(m_a):
        raise ValueError(
            "Scalar operands are not allowed, use '*' instead"
        )

    if np.isscalar(m_b):
        raise ValueError(
            "Scalar operands are not allowed, use '*' instead"
        )

    return np.matmul(m_a, m_b)
