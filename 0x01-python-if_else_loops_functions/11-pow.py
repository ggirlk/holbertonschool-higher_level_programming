#!/usr/bin/python3
def pow(a, b):
    if (b == 0): return 1
    elif (int(b % 2) == 0): 
        return (pow(a, int(b / 2)) *
               pow(a, int(b / 2))) 
    else: 
        return (a * pow(a, int(b / 2)) *
                   pow(a, int(b / 2)))
