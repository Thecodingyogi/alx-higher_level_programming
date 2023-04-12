#!/usr/bin/python3

"""Defines a function that returns the dictionary description"""


def class_to_json(obj):
    """Returns:
            The dictionary description with simple data structure for
            JSON serialization of an object.
    """
    return obj.__dict__
