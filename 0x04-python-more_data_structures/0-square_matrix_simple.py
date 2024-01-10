#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[num for num in row] for row in matrix]
    r = len(new)
    for i in range(r):
        c = len(new[i])
        for j in range(c):
            new[i][j] *= new[i][j]
    return new
