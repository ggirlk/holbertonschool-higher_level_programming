#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    s = list(a_dictionary)
    for i in sorted(s):
        if i == key:
            setattr(a_dictionary, i, value)
    return a_dictionary
