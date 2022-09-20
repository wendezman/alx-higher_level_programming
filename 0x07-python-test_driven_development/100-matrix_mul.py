#!/usr/bin/python3
"""
matrix mul module
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        product of two matrices
    """

    orig_len = 0
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    for blocks in m_a:
        if type(blocks) is not list:
            raise TypeError("m_a must be a list of lists")
        if not blocks:
            raise ValueError("m_a can't be empty")
        for integers in blocks:
            if type(integers) is not int and type(integers) is not float:
                raise TypeError("m_a should contain only integers or floats")
        if len(blocks) != orig_len and orig_len != 0:
            raise TypeError("each row of m_a must be of the same size")
        orig_len = len(blocks)

    orig_len = 0
    for blocks in m_b:
        if type(blocks) is not list:
            raise TypeError("m_b must be a list of lists")
        if not blocks:
            raise ValueError("m_b can't be empty")
        for integers in blocks:
            if type(integers) is not int and type(integers) is not float:
                raise TypeError("m_b should contain only integers or floats")
        if len(blocks) != orig_len and orig_len != 0:
            raise TypeError("each row of m_b must be of the same size")
        orig_len = len(blocks)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_list = list()
    for row_a in range(len(m_a)):
        flag = 0
        inner_list = list()
        for row_b in range(len(m_b)):
            for col in range(len(m_b[row_b])):
                if flag == 0:
                    inner_list.append(m_a[row_a][row_b] * m_b[row_b][col])
                else:
                    inner_list[col] += (m_a[row_a][row_b] * m_b[row_b][col])
            flag = 1
        result_list.append(inner_list)

    return result_list
