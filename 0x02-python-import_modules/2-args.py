#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    argv = sys.argv
    print("{:d} arguments:".format(len(argv) - 1))
    while i != len(argv):
        print("{:d}: {}".format(i, argv[i]))
        i += 1
