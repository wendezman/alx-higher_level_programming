#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda one_D: list(map(lambda x: x**2, one_D)), matrix))
