#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        i = 0
        if nb_lines <= 0:
            print(f.read(), flush=True)
        else:
            while i <= nb_lines:
                print(f.readline(), end="", flush=True)
                i+= 1
        f.close()
