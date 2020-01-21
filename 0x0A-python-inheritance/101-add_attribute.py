#!/usr/bin/python3
def add_attribute(obj, attr, val):
    testattr(obj, attr, val)


def testattr(obj, attr, val):
    try:
        setattr(obj, attr, val)
    except:
        raise TypeError("can't add new attribute")
