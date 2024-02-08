#!/usr/bin/python3
"""
BaseGeometry class module.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.
    """

    def area(self):
        """
        Calculate the area. This method should be overridden by subclasses.

        Raises:
        Exception: Always raises an exception with the message
        "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if 'value' is an integer and satisfies specific conditions.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' does not satisfy specific conditions.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
