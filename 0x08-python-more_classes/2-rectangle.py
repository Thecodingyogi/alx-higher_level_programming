#!/usr/bin/python3

"""Defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return (self.__width * self__height)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
