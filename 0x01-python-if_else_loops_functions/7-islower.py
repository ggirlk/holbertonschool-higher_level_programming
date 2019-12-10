#!/usr/bin/env python3
def islower(c):
    for i in range(97, 122):
        if ord(c) == i:
            return True
        else:
            return False
