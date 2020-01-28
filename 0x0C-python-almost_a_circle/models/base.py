#!/usr/bin/python3
import json


class Base():

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open(self+'.json', 'w') as f:
            f.write('yes')
