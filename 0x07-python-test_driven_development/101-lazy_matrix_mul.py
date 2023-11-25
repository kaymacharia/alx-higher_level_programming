#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Creates a function for matrix multiplication utilizing NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
"""Provide the product of two matrices.
Parameters:

m_a (list of lists containing integers/floats): Represents the first matrix.
m_b (list of lists containing integers/floats): Represents the second matrix.
"""

return (np.matmul(m_a, m_b))
