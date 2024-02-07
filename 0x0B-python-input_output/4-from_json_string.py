#!/usr/bin/python3
"""
Module contains a function that
returns an object represented by a JSON string
"""
import json
"""json module"""


def from_json_string(my_str):
    """
    Function returns the object represented by a JSON string
    args:
    my_str: the string to be converted
    returns:
    an object
    """
    return json.loads(my_str)
