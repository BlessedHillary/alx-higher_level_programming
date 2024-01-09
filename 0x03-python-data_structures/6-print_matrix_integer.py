#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    r = len(matrix)
    for i in range(r):
        c = len(matrix[i])
        for j in range(c):
            if j != c - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]), end='')
        print()
