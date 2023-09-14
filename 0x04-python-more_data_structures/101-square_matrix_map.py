#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda L: map(lambda x: x * x, L), matrix))
