#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = ""
    for i in text:
        if s == "" and i == " ":
            pass
        else:
            s += i
        if (i == ".") or (i == "?"):
            print(s)
            print()
            s = ""
