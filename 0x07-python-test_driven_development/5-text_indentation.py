#!/usr/bin/python3
"""
module contains a function that splits lines based on .,?,:
"""


def text_indentation(text):
    """
    Split and print text into lines based on ".", "?",
    and ":" without using string methods.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input 'text' is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = ""
    for char in text:
        s += char
        if char in ".?:":
            print(s.strip(), end="\n\n")
            s = ""
    print(s.strip(), end="")
