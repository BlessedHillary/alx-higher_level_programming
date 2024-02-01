#!/usr/bin/python3

"""
Function that divides all the integers in a matrix by another number (div)
"""


def matrix_divided(matrix, div):
    """
    function divides integers in a matrix by a number (div)
    Takes two arguments
    Raises:
        TypeError when rows of a matrix are not equal
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise ValueError("The matrix cannot be empty")
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
            val = round(num / div, 2)
            new_row.append(val)
        new_matrix.append(new_row)
    return new_matrix
