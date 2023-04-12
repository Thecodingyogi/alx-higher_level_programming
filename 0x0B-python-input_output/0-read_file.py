#!/usr/bin/python3

"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file"""
    with open('UTF8', 'r', encoding='utf-8') as file:
        print(file.read())
