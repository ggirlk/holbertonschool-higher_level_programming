#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in range(0, len(matrix)):
        newMatrix.append(list(map(lambda x: x ** 2, matrix[i])))
    return newMatrix
