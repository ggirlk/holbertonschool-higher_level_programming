#!/usr/bin/python3
def search_replace(my_list, search, replace):
     i = 0
     newl = [0] * len(my_list)
     while i != len(my_list):
         if my_list[i] == search:
             newl[i] = replace
         else:
             newl[i] = my_list[i]
         i += 1
     return newl
