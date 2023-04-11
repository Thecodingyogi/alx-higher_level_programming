#!/usr/bin/python3

"""Defines a class BaseGeometry and subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
        Args:
            width: Must be a positive integer
            height: Must be a positive integer
    """
    def __init__(self, width, height):
        """Initializes a rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of te Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
