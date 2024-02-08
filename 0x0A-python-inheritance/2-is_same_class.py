#!/usr/bin/python3

"""
Module has one function
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare the object's type with.

    Returns:
    bool: True if the object is an instance of the specified class,
    False otherwise.
    """
    return type(obj) is a_class
