#!/usr/bin/python3
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            d = dict()
            for i in attrs:
                d = dict(
                      (key, value)
                      for (key, value) in self.__dict__.items()
                      if key in attrs)
            return d
        else:
            return self.__dict__
