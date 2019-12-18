#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        a = ""
        for j in range(0, len(matrix[i])):
            if matrix[i][j] in range(0, 1000000):
                a += format(matrix[i][j])
                if j < len(matrix[i]) - 1:
                    a += " "
        print("{}".format(a))
