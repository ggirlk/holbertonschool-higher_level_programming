#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            my_list[i]
        except IndexError:
            print()
            break
        else:
            print(my_list[i], end="")
        i += 1
    return (i)
