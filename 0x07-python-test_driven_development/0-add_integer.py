#!/usr/bin/python3
""" This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer() For example;
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """ adding 2 integers
        a: integer
        b: integer and if not specified it took 98 """
    t = 0
    if a != None or isinstance(a, float) or isinstance(a, int):
        a = int(a)
    else:
        t = 1
        raise TypeError('a must be an integer')
    if b != None or isinstance(b, float) or isinstance(b, int):
        b = int(b)
    else:
        t = 1
        raise TypeError('b must be an integer')
    if t == 0:
        return (a + b)
