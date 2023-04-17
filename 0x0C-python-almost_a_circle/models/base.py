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
