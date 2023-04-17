#!/usr/bin/python3

"""Defines unittests for base.py"""

import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests to test the Base class"""

    def test_no_arg(self):
        """Test if no argument is passed"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_None(self):
        """Test when None argument is passed"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Test a uniques id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_public_id(self):
        """Test public id"""
        b = Base(12)
        b.id = 31
        self.assertEqual(b.id, 31)

    def test_two_args(self):
        """Test two args"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_nb_instances_after_unique_id(self):
        """Test number of instances after unique id is added"""
        b = Base()
        b1 = Base(31)
        b2 = Base()
        self.assertEqual(b.id, b2.id - 1)

if __name__ == '__main__':
    unittest.main()
