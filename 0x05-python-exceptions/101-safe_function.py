#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        f = fct(*args)
        return f
    except (ZeroDivisionError, IndexError) as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
