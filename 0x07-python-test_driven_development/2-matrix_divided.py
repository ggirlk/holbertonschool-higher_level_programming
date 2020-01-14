#!/usr/bin/python3
""" This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided() For example;
>>> matrix = [[1, 2, 3],[4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ adding 2 integers
        matrix: list of integers or floats
        div: number
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    l0 = []
    i = len(matrix[0])
    for mx in matrix:
        l1 = []
        if len(mx) != i:
            raise TypeError('Each row of the matrix must have the same size')        
        for my in mx:
            if not (isinstance(my, float) or isinstance(my, int)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            r = my/div
            r = int(r * 100)
            r = r / 100
            l1.append(r)
        l0.append(l1)
    return (l0)
