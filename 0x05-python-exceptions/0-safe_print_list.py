#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    k = 0
    while i < x:
        try:
            my_list[i]
        except:
            break
        else:
            k += 1
            print(my_list[i], end="")
        i += 1
    if x != 0:
        print()
    return (k)
