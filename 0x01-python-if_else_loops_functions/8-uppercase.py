#!/usr/bin/python3
def uppercase(str):
    string = ''
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s)-32)
            string += s
        else:
            string += s
    print("{:s}\n".format(string), end='')
