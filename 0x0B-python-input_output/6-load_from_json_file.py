#!/usr/bin/python3

"""Defines a function that creates an object"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
