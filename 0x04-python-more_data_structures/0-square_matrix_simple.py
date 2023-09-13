#!/usr/bin/python3
def square_number(a):
    return a * a


def square_matrix_simple(matrix=[]):
    temp = matrix.copy()
    for i in range(0, len(matrix)):
        temp[i] = list(map(square_number, matrix[i]))
    return temp
