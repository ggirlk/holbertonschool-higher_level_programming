#!/usr/bin/env python3
def islower(c):
    min = range(97, 122)
    if ord(c) in min:
        return True
    else:
        return False
