#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        i = 0
        while f.readline():
            i+= 1
        f.close()
    return i


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r", encoding="utf-8") as f:
        l = []
        i = 0
        s = ""
        while i <= number_of_lines(filename):
            line = f.readline()
            #l.append(f.readline())
            s += line
            if search_string in line:
                s += new_string
                l.append(line)
            i+=1
        f.close()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)
        f.close()
