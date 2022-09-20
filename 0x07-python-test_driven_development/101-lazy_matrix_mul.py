#!/usr/bin/python3
"""
lazy matrix mul module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module numpy
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        product of two matrices
    """
    return np.matmul(m_a, m_b)
