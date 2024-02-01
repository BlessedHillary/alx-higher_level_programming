#!/usr/bin/python3
"""
Function that prints someones first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function takes two arguments and prints the output
    """
    if last_name != "":
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
