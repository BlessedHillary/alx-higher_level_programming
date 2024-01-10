#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sys.argv[0] = "argument"
    total_argv = 1
    n = len(sys.argv)
    b = len(sys.argv) - 1
    if b == 0:
        print("{} {}s.".format(b, sys.argv[0]))
    elif b == 1:
        print("{} {}:".format(b, sys.argv[0]))
    else:
        print("{} {}s:".format(b, sys.argv[0]))
    for x in range(1, n):
        print("{}: {}".format(x, sys.argv[x]))
