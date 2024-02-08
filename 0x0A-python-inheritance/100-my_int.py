#!/usr/bin/python3

"""MyInt class module"""


class MyInt(int):
    """
    A class that inherits from int and customizes the
    behavior of equality operators.
    """

    def __eq__(self, other):
        """
        Customize the behavior of the == operator.

        Args:
        other (int): The integer to compare with.

        Returns:
        bool: True if the values are not equal, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Customize the behavior of the != operator.

        Args:
        other (int): The integer to compare with.

        Returns:
        bool: True if the values are equal, False otherwise.
        """
        return int(self) == other
