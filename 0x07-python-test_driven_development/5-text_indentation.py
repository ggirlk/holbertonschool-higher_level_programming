#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = ""
    k = 0
    for i in text:
        if s == "" and i == " ":
            pass
        else:
            s += i
        if (i == ".") or (i == "?"):
            k = 1
            print(s)
            print()
            s = ""
    if k == 0:
        print(text)
        print()
