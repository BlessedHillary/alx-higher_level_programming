#!/usr/bin/python3
""" Class square that defines a square"""


class Square:
    """
    Square class size


    Attributes:
        __size(int): Size of the square

    Methods:
        __init__(self, size): Initializes a Square instance
    """
    def __init__(self, size=0):
        """ Initializes a new square instance

        Args:
            size(int): size of square

        Raises:
            TypeError: If size is not of type int
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
