#!/usr/bin/python3

"""Contains the class MyList"""


class MyList(list):
    """Subclass of list"""
    def __init__(self):
        """Initializes MyList"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list in ascending sort"""
        print(sorted(self))
