#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.
The module provides one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices after thorough type and shape validation.

    Args:
        m_a: The first matrix (list of lists of integers/floats).
        m_b: The second matrix (list of lists of integers/floats).

    Raises:
        TypeError: If requirements regarding lists, nesting, types,
                   or row equality are violated.
        ValueError: If matrices are empty or mathematically unmultipliable.

    Returns:
        A new matrix representing the matrix product of m_a and m_b.
    """
    # 1. Verify m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Verify m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Verify m_a and m_b are not empty ([] or [[]])
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # 4. Verify elements are strictly integers or floats (excluding booleans)
    for row in m_a:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    # 5. Verify rectangular consistency (all rows must have identical size)
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Verify multiplication compatibility (cols of m_a == rows of m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7. Perform matrix multiplication calculation
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row_result.append(total)
        result.append(row_result)

    return result
