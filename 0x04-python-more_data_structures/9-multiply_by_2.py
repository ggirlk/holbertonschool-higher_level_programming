#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = list(a_dictionary)
    nw = {}
    for i in s:
        nw[i] = a_dictionary[i] * 2
    return nw
