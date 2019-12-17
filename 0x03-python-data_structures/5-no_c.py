#!/usr/bin/env python3
def no_c(my_string):
    nstr = [""] * len(my_string)
    for i in range(0, len(my_string)):
        if (my_string[i] != "c" and my_string[i] != "C"):
            nstr[i] = my_string[i]
    return "".join(nstr)
