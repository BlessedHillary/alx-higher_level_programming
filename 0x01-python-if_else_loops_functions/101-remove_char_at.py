#!/usr/bin/python3
def remove_char_at(str, n):
    string = ''
    for s in range(len(str)):
        if s != n:
            string += str[s]
    return string
