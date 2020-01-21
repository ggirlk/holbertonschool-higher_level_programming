#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        l = list(self)
        l.sort()
        print(l)
