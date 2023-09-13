#!/usr/bin/python3
def square_number(a):
    return a**2


def square_matrix_simple(matrix=[]):
    temp = [[]]
    for i in range(0, len(matrix)):
        temp[i] = list(map(square_number, matrix[i]))
    return temp
