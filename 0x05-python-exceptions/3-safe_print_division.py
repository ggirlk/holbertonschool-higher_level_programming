#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        int(a) & int(b)
    except ValueError:
        print("Inside result: None")
        return (None)
    finally:
        if (b != 0):
            r = a/b
            print("Inside result: {}".format(r))
            return (r)
        else:
            print("Inside result: None")
            return (None)
