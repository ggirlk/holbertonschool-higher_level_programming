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

    def save_to_file(cls, list_objs):
        """ 'save_to_file' save an obj to a json file """
        with open(self+'.json', 'w') as f:
            f.write('yes')
