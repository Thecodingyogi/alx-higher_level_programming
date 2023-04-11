#!/usr/bin/python3

"""Defines a class BaseGeometry and subclass Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle class.

        Args:
            width: Must be private and positive integers
            height: Must be private and positive integers
    """
    def __init__(self, width, height):
        """Initializes a rectangle"""
        self.__width = width
        self.__height = height
        integer_validator("width", width)
        integer_validator("height", height)
