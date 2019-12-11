#!/usr/bin/python3
def uppercase(str):
    i = 0
    k = 0
    _end = ""
    while i != len(str):
        a = 97
        b = 65
        k = 0
        if i == len(str) - 1 :
            _end = "\n"
        while a != 123:
            if ord(str[i]) == a or ord(str[i]) == b:
                k = 1
                print("{:c}".format(b), end=_end)
            a += 1
            b += 1
        if k == 0:
            print("{}".format(str[i]), end=_end)
        i += 1
