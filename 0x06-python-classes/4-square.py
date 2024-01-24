#!/usr/bin/python3
""" Class square that defines a square"""


class Square:
    """
    Square class size


    Attributes:
        __size(int): Size of the square

    Methods:
        __init__(self, size): Initializes a Square instance
        area(self): Returns the current square area
        size(self): Getter method
        size(self, value): Setter method
    """
    def __init__(self, size=0):
        """ Initializes a new square instance """
        self.__size = size

    @property
    def size(self):
        """
        Getter method

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Initializes a public instance method that returns the square

        Returns:
            int: area of square
        """
        return self.__size ** 2
