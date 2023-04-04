#!/usr/bin/python3

"""Defines a square."""


def print_square(size):
    """Prints a square with the character #
        Args:
            size: size length of the square.
        Exceptions:
            TypeError: If size is a float and less than 0.
            ValuError: If size is less than 0.
    """
    if not isinstance(size, int) or ((isinstance(size, float)) and (size < 0)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
