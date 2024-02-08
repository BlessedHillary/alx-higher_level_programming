#!/usr/bin/python3

"""Import the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing squares, inheriting from the Rectangle class.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with the provided size.

        Args:
        size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: The string representation in the format "[Square] <size>/<size>".
        """
        return str("[Square] {:d}/{:d}".format(self.__size, self.__size))
