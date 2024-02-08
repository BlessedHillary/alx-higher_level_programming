#!/usr/bin/python3
"""
Rectangle class module based on 7-base_geometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of BaseGeometry for representing rectangles.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: The string representation in the format
        "[Rectangle] <width>/<height>".
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
