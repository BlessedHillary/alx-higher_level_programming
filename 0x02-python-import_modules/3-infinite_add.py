#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    total_argv = 0
    for x in range(1, n):
        total_argv += int(sys.argv[x])
    print("{}".format(total_argv))
