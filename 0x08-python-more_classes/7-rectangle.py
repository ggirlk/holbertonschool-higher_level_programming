#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height*self.__width)

    def perimeter(self):
        return (2*self.__height+2*self.__width)

    def __str__(self):
        strn = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                strn += str(self.print_symbol)
            if i < self.__height - 1:
                strn += '\n'
        return (strn)

    def __repr__(self):
        return ("Rectangle("+str(self.__width)+", "+str(self.__height)+")")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
