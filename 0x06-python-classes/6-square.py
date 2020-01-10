
#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) != tuple & len(value) != 2 &
            type(value[0]) != int & type(value[1]) != int &
                value[0] < 0 & value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
