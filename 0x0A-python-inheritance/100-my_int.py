#!/usr/bin/python3

"""Defines a class Myint"""


class Myint(int):
    """Represents a Rebel"""

    def __eq__(self, value):
        """!= changes to =="""
        return self.int != value

    def __ne__(self, value):
        """changes == to !="""
        return self.int == value
