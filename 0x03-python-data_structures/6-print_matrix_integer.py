#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for array in matrix:
        print(" ".join("{:d}".format(element) for element in array))
