#!/usr/bin/python3

"""Defines a function that writes a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file(UTF8)

    Returns:
            The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
