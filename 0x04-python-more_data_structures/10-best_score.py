#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    nw = []
    for i in a_dictionary:
        nw.append(i)
    return max(nw)
