#!/usr/bin/python3
"""
matrix divided module
"""


def matrix_divided(matrix, div):
    """
    divides elements of a matrix
    Args:
        matrix: matrix before division
        div: divisor
    Returns:
        matrix containing elements of the original
        matrix divided by div rounded to two
        decimal places
    """
    orig_leng = 0
    messege_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(messege_err)

    for block in matrix:
        if type(block) is not list:
            raise TypeError(messege_err)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(messege_err)

        if len(block) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        orig_leng = len(block)
    
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
