#!/usr/bin/python3

"""
Module Class to JSON
"""


def class_to_json(obj):
    """
    function returns the dictionary description with
    simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    args:
        obj: an instance of a Class
    """

    return obj.__dict__
