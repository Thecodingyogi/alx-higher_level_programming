#!/usr/bin/python3

"""Defines a class Base"""
import json


class Base:
    """Represents the base

        Attributes:
            __nb_objects: Private class attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8')as jsonfile:
            if list_objs is None or list_objs == '[]':
                jsonfile.write("[]")
            else:
                list_dict = [x.to_dictionary() for x in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == '[]':
            return "[]"
        else:
            return json.loads(json_string)
