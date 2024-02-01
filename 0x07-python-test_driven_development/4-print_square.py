#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    Print a square of a given size using '#' characters.

    Parameters:
        size (int): The size of the square. It must be a non-negative integer.

    Raises:
        TypeError: If `size` is not an integer or is a negative float.
        ValueError: If `size` is a negative integer.

    Returns:
        None

    Example:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
