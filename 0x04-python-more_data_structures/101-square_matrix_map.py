#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda ko: list(map(lambda x: x * x, ko)), matrix))
