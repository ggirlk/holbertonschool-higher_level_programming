#!/usr/bin/python3
""" Base Module
    is the parent of all shapes
"""

import json


class Base():
    """class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ '__init__' Base constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ 'to_json_string' a static method that
        convert a dictionary list to json string """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ 'save_to_file' save an obj to a json file """
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None:
                s = "[]"
            else:
                s = cls.to_json_string([i.__dict__ for i in list_objs])
            f.write(s)

    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        return json.loads(json_string)
