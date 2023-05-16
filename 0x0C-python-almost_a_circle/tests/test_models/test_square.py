#!/usr/bin/python3

"""Unittests for square that inherits from the Rectangle class"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_instatiation(unittest.TestCase):
    """Tests the Square class"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_Rectangle(self):
        self.assertIsInstance(Square(14), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s = Square(6)
        s1 = Square(7)
        self.assertEqual(s.id, s1.id - 1)

    def test_two_args(self):
        s = Square(6, 1)
        s1 = Square(7, 1)
        self.assertEqual(s.id, s1.id - 1)

    def test_three_args(self):
        s = Square(9, 2, 1)
        s1 = Square(8, 3, 4)
        self.assertEqual(s.id, s1.id - 1)

    def test_four_args(self):
        s = Square(9, 3, 4, 10)
        self.assertEqual(10, s.id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(9, 8, 7, 6, 5)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(6, Square(6, 29, 14, 4).size)

    def test_size_setter(self):
        s = Square(4, 5, 10, 12)
        s.size = 8
        self.assertEqual(8, s.size)


class TestSquare_size(unittest.TestCase):
    """Tests the size initializationof the Square class"""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(9.2)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('Cynthia')

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(True)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([8, 1])

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(range(10))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-6, 1)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0, 3)


class TestSquare_x(unittest.TestCase):
    """Tests the x argument"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, None)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, 'Cynthia')

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, 7.9)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, [2, 4, 6])

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, True)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, complex(3))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(2, -2)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(2, range(7))


class TestSquare_y(unittest.TestCase):
    """Tests y in theSquare class"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, None)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, 1.2)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, 'Tonui')

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, [2, 4])

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(2, 4, -2)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, complex(14))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, range(3))

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(2, 4, True)


class TestSquare_area(unittest.TestCase):
    """Tests the area method of the Square class"""

    def test_area(self):
        self.assertEqual(81, Square(9, 0, 0).area())

    def test_area_change_size(self):
        s = Square(5, 0, 0, 1)
        s.size = 6
        self.assertEqual(36, s.area())

    def test_area_one_arg(self):
        s = Square(2, 3, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_update_args(unittest.TestCase):
    """Tests the update args of the Square class"""

    def test_update_zero_args(self):
        s = Square(1, 2, 3, 4)
        s.update()
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')

    def test_update_one_args(self):
        s = Square(1, 2, 3, 4)
        s.update(23)
        self.assertEqual(str(s), '[Square] (23) 2/3 - 1')

    def test_update_two_args(self):
        s = Square(1, 2, 3, 4)
        s.update(23, 14)
        self.assertEqual(str(s), '[Square] (23) 2/3 - 14')

    def test_update_three_args(self):
        s = Square(1, 2, 3, 4)
        s.update(23, 14, 5)
        self.assertEqual(str(s), '[Square] (23) 5/3 - 14')

    def test_update_four_args(self):
        s = Square(1, 2, 3, 4)
        s.update(23, 14, 5, 1)
        self.assertEqual(str(s), '[Square] (23) 5/1 - 14')

    def test_update_more_than_four(self):
        s = Square(1, 2, 3, 4)
        s.update(23, 14, 5, 1, 2)
        self.assertEqual(str(s), '[Square] (23) 5/1 - 14')

    def test_update_args_width_setter(self):
        s = Square(12, 12, 10, 10)
        s.update(89, 3)
        self.assertEqual(3, s.width)

    def test_update_args_height_setter(self):
        s = Square(12, 12, 10, 10)
        s.update(12, 2)
        self.assertEqual(2, s.height)

    def test_update_args_size_str(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.update(12, 'string')

    def test_update_args_size_negative(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(12, -9)

    def test_update_args_size_zero(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(12, 0)

    def test_update_args_x_str(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s.update(12, 5, 'string')

    def test_update_args_x_negative(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s.update(12, 5, -1)

    def test_update_args_y_str(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s.update(12, 5, 12, 'string')


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs in Square class"""

    def test_update_kwargs_one(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2)
        self.assertEqual('[Square] (2) 12/12 - 12', str(s))

    def test_update_kwargs_two(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2, size=3)
        self.assertEqual('[Square] (2) 12/12 - 3', str(s))

    def test_update_kwargs_three(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2, size=3, x=4)
        self.assertEqual('[Square] (2) 4/12 - 3', str(s))

    def test_update_kwargs_four(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual('[Square] (2) 4/5 - 3', str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(12, 12, 12, 12)
        s.update(id=2, size=11)
        self.assertEqual(11, s.height)

    def test_update_kwargs_None(self):
        s = Square(12, 12, 12, 12)
        s.update(id=None)
        updated = '[Square] ({}) 12/12 - 12'.format(s.id)
        self.assertEqual(updated, str(s))

    def test_update_kwargs_size_negative(self):
        s = Square(12, 12, 12, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(size=-2)

    def test_update_kwargs_x_negative(self):
        s = Square(12, 12, 12, 12)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s.update(x=-8)

    def test_update_kwargs_y_negative(self):
        s = Square(12, 12, 12, 12)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s.update(y=-8)


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests the dictionary in the Square class"""
    def test_to_dictionary_output(self):
        s = Square(10, 11, 1, 1)
        dict1 = {'size': 10, 'x': 11, 'y': 1, 'id': 1}


if __name__ == '__main__':
    unittest.main()
