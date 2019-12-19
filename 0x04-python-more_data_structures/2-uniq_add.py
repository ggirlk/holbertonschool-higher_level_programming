#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    a = 0
    for i in range(0, len(my_list)):
        a += my_list[i]
    return a
