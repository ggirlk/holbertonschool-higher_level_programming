#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        i = 0
        while f.readline():
            i += 1
        f.close()
    return i


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        i = 0
        nb = number_of_lines(filename)
        if nb_lines <= 0 or nb <= nb_lines:
            print(f.read())
        else:
            while i < nb_lines:
                print(f.readline(), end="")
                i += 1
        f.close()
