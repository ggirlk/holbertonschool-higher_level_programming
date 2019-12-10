#!/usr/bin/python3
a = 0
_end = ", "
while a != 10:
    b = a
    while b != 10: 
        if a != b:
            print("{:d}{:d}".format(a, b), end = "")
            if a == 8:
                _end = "\n"
            print("{}".format(_end), end = "")
        b += 1
    a += 1
