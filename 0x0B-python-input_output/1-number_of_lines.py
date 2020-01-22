#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        i = 0
        while f.readline():
            i+= 1
        f.close()
    return i
