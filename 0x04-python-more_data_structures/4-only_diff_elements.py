#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1 = list(set_1)
    set_2 = list(set_2)
    s = set_1 + set_2
    s = list(set(s) - (set(set_2) & set(set_1)))
    return s
