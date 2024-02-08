#!/usr/bin/python3

"""
A function that adds a new attribute to an object if it's possible.
"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
    obj (object): The object to which the attribute should be added.
    name (str): The name of the attribute to be added.
    value: The value to assign to the attribute.

    Raises:
    TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
