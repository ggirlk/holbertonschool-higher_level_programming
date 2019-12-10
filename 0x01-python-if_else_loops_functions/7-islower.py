#!/usr/bin/env python3
def islower(c):
    i = 97
    while i != 123:
        if ord(c) == i:
            return True
        else:
            return False
        i += 1
