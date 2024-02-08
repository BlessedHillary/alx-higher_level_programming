#!/usr/bin/python3
"""
Module contains one function
"""


def lookup(obj):
    """
    function takes one arg
    returns a list of attributes and objects
    """
    lookup_list = []
    for att in dir(obj):
        lookup_list.append(att)
    return lookup_list
