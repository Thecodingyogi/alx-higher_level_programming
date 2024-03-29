#!/usr/bin/python3

"""Defines a function that returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Returns:
            Representation of an object(string)
    """
    return json.dumps(my_obj)
