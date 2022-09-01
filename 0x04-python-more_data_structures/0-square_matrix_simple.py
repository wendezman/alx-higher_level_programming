#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda one_D_mat: list(map(lambda x: x * x, one_D_mat)), matrix))
