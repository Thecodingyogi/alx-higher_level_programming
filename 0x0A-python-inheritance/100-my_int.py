#!/usr/bin/python3

"""Defines a class Myint"""
MyInt = __import__('100-my_int').MyInt


class Myint(int):
    """Represents a Rebel"""
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= changes to =="""
        return int(self) != other

    def __ne__(self, other):
        """changes == to !="""
        return int(self) == other
