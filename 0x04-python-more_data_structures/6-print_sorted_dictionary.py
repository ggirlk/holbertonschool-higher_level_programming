#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = list(a_dictionary);
    #s = list(s.sort())
    for i in sorted(s):
        print("{} : {}".format(i, a_dictionary.get(i)))
