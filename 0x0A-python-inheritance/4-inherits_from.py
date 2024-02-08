#!/usr/bin/python3
"""
Module contains a function for checking if an object is an instance of
a class that inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from a specified class.

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare with.

    Returns:
    bool: True if the object is an instance of a class that inherits
    from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
