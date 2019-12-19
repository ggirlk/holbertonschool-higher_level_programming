#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = [[0] * len(matrix[0])] * len(matrix)
    #newMatrix.append()
    #for i in range(0, len(matrix)):
       #newMatrix.append(matrix[i])
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            a = matrix[i][j] * matrix[i][j]
            newMatrix[i][j] = a
    return newMatrix
