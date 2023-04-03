#!/usr/bin/python3

"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """Returns the addition of two numbers

        The two numbers must be integers or floats otherwise
        a TypeError exception will be raised.

        The numbers must be first casted to integers if they
        are float."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
