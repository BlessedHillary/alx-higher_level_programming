#!/usr/bin/python3
"""
Module contains a function that writes to a file
"""


def append_write(filename="", text=""):
    """
    Function appends to a file, creates new file if doesnt exist
    args:
        filename: the name of the file to append to
        text: the tect to append
    returns: number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        file_a = f.write(text)
        return file_a
