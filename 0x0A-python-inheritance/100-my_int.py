#!/usr/bin/python3

"""Defines a class Myint"""
MyInt = __import__('100-my_int').MyInt


class Myint(int):
    """Represents a Rebel"""

    def __eq__(self, value):
        """!= changes to =="""
        return int(self) != value

    def __ne__(self, value):
        """changes == to !="""
        return int(self) == value
