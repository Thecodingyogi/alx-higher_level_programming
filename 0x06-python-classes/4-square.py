#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): Size of new square
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter of __size
            Args:
                value (int): size of the square.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
