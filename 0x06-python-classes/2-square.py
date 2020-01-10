#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if isinstance(size, int):
                raise TypeError("size must be an integer")
        except ValueError as ex:
            print(ex)
        except TypeError as ex:
            print(ex)
        self.__size = size
