#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        stdout = open(1, 'w')
        print(f.read(), file=stdout)
        f.close()
