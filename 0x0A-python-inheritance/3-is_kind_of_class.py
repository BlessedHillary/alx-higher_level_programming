#!/usr/bin/python3
"""
module contains one function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or a subclass of a specific class.

    Args:
    obj (object): The object to be checked.
    a_class (type): The class to compare the object's type with.

    Returns:
    bool: True if the object is an instance of the specified class or
    its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
