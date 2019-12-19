#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    s = list(a_dictionary)
    for i in s:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
