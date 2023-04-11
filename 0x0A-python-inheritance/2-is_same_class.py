#!usr/bin/python3

"""Defines a function"""


def is_same_class(obj, a_class):
    """Returns:
            True: if object is exactly an instance of the specified class
            False: otherwise.
    """
    if (type(obj) == a_class):
        return True
    return False
