#!/usr/bin/python3
"""
module contains one function
"""
import json
"""import json"""


def load_from_json_file(filename):
    """
    function  that creates an object from an object file
    takes one argument
    """
    with open(filename, 'r') as f:
        x = json.load(f)
        return x
