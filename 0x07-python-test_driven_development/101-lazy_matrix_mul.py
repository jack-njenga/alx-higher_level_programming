#!/usr/bin/python3

"""
Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy

    Args:
        m_a (list of list or matrix): first matrix
        m_b (list of list or matrix): second matrix
    """
    try:
        result = np.matmul(m_a, m_b)
    except Exception as e:
        print(e)

    return result
