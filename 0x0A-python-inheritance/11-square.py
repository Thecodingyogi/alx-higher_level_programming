#!/usr/bin/python3

"""Defines a square that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class
        Args:
            size: must be private and a positive integer.
    """
    def __init__(self, size):
        """Initializes the square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """The square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
