#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda oneDmat: list(map(lambda x: x**2, oneDmat)), matrix))
