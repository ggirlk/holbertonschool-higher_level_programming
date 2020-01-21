#!/usr/bin/python3
class MyInt(int):
    """ class MyInt """

    def __new__(cls, *args, **kwargs):
        m = str(args[0])
        return m
