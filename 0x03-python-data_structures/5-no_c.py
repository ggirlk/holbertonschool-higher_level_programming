#!/usr/bin/python3
def no_c(my_string):
    nstr = ""
    for i in range(0, len(my_string)):	
        if (my_string[i] != "c" and my_string[i] != "C"):	
            nstr += my_string[i]	
    my_string = nstr
    return my_string
