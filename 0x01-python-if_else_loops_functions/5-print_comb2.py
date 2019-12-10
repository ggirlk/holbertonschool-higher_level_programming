#!/usr/bin/python3
a = 0
_end = ", "
while a != 100:
    print("{:02d}".format(a), end = "")
    if a == 99:
        _end = "\n"
    print("{}".format(_end), end = "")
    a += 1
