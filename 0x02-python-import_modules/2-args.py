#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 0
    while i != len(sys.argv):
        print("{:d}: {}".format(i, sys.argv[i]))
        i += 1
