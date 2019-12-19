#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in sorted(a_dictionary):
        if str(i) == key:
            del a_dictionary[key]
    return a_dictionary
