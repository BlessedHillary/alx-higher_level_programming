#!/usr/bin/python3
"""
Module contains one function
"""


def read_file(filename=""):
    """
    Functions reads a file and prints to stdout
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
