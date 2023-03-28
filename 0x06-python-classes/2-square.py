#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): Size of the new square.
        """

        if type(size) not int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
