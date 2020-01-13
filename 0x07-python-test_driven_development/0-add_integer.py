#!/usr/bin/python3
""" This is the "add_integer" module.
The add_integer module supplies one function, add_integer().  For example,
>>> add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """ adding 2 integers
        a: integer
        b: integer and if not specified it took 98
        return: sum of a + b
    """
    try:
        a = int(a)
        b = int(b)
        return (a + b)
    except:
        if not isinstance(a, int):
            raise TypeError('a must be an integer')
        if not isinstance(b, int):
            raise TypeError('b must be an integer')
