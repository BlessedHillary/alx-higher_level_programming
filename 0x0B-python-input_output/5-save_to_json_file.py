#!/usr/bin/python3
"""
Module
"""
import json
"""
import json
"""


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to a text file using
    a  JSON representation
    takes two arguments
    """
    with open(filename, 'w') as f:

        json.dump(my_obj, f)
