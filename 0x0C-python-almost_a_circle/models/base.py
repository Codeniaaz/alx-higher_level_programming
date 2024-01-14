#!/usr/bin/python3
""" module for Base class """

import json
class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not None, assign the public instance attribute id
        with this argument value - you can assume id is an integer
        and you don’t need to test the type of it
        otherwise, increment __nb_objects and assign the new value 
        to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "":
            return ""
        else:
            return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs= []
        else:
            list_objs = type(list_objs)
        a = "{}.json".format(list_objs.__name__)
        with open(a, "w") as f:
            f.write(cls.to_json_string(list_objs))
