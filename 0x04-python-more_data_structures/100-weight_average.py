#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    a = b = pr = av = 0
    for i in my_list:
        a += i[1]
        pr = i[0] * i[1]
        b += pr
        av = b / a
    return av
