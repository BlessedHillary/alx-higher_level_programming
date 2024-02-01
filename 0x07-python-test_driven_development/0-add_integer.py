#!/usr/bin/python3

"""
This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    Function adds two integers
    args:
          a(int) first argument
          b(int) second argument. if not provided, default = 98
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
