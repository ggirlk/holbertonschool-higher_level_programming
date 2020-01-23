#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        i = 0
        if nb_lines <= 0:
            print(f.read())
        else:
            while i < nb_lines:
                print(f.readline(), end="")
                i+= 1
