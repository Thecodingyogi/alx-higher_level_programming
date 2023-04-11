#!/usr/bin/python3

"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Represents BaseGeometry class"""
    def area(self):
        """Defines an area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines an function that validates an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
