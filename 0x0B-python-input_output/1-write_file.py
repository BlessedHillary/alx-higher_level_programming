#!/usr/bin/python3
"""
Module has one function
"""


def write_file(filename="", text=""):
    """
    function writes to a file and returns number of chars written
    creates a new file if file doesnt exist
    overwrites file content if file exists
    Args:
        text(str): The string to write to file
        filename: the file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_f = f.write(text)
        return write_f
