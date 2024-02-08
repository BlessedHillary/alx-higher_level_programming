#!/usr/bin/python3
"""
Square class module based on 9-rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass of Rectangle for representing squares.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with the size.

        Args:
        size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns:
        area of a square
        """
        return self.__size ** 2
