#!/usr/bin/python3

"""Testing the rectangle.py file"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_instantiation(unittest.TestCase):
    """Testing the rectangle class"""
    def test_rectangle_is_base(self):
        """Tests if the Rectangle class inherits from the Base class."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_width_getter(self):
        """Tests the width getter"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(10, r.width)

    def test_width_setter(self):
        """Tests the width setter"""
        r = Rectangle(10, 2, 0, 0, 12)
        r.width = 15
        self.assertEqual(r.width, 15)

    def test_width_private(self):
        """Tests if width attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__width)

    def test_height_getter(self):
        """Tests the height getter"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(2, r.height)

    def test_height_setter(self):
        """Tests the height setter"""
        r = Rectangle(10, 2, 0, 0, 12)
        r.height = 6
        self.assertEqual(r.height, 6)

    def test_height_private(self):
        """Tests if height attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__height)

    def test_x_getter(self):
        """Tests the x getter"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(0, r.x)

    def test_x_setter(self):
        """Tests the x setter"""
        r = Rectangle(10, 2, 0, 0, 12)
        r.x = 29
        self.assertEqual(r.x, 29)

    def test_x_private(self):
        """Tests if x attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__x)

    def test_y_getter(self):
        """Tests the y getter"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(0, r.y)

    def test_y_setter(self):
        """Tests the y setter"""
        r = Rectangle(10, 2, 0, 0, 12)
        r.y = 14
        self.assertEqual(r.y, 14)

    def test_y_private(self):
        """Tests if y attribute is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__y)

    def test_no_args(self):
        """Tests when no argument is not passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test when one argument is passed"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test two arguments"""
        r = Rectangle(10, 2)
        r1 = Rectangle(2, 10)
        self.assertEqual(r.id, r1.id - 1)

    def test_three_args(self):
        """Test three arguments"""
        r = Rectangle(10, 2, 0)
        r1 = Rectangle(2, 10, 0)
        self.assertEqual(r.id, r1.id - 1)

    def test_four_args(self):
        """Test four arguments"""
        r = Rectangle(10, 2, 0, 0)
        r1 = Rectangle(2, 10, 0, 0)
        self.assertEqual(r.id, r1.id - 1)

    def test_five_args(self):
        """Test five arguments"""
        self.assertEqual(12, Rectangle(10, 2, 0, 0, 12).id)

    def test_more_than_five_args(self):
        """Test more than five arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 14)


class TestRectangle_width(unittest.TestCase):
    """Unittests to test width attribute"""
    def test_None_width(self):
        """Tests when None is passed as width"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(None, 2)

    def test_str_width(self):
        """Tests if a string is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('String', 10)

    def test_float_width(self):
        """Tests if a float is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(3.9, 8)

    def test_list_width(self):
        """Tests if list is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle([2, 3, 4], 9)

    def test_tuple_width(self):
        """Tests if tuple was passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle((8, 4, 3), 1)

    def test_range_width(self):
        """Tests if range is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(range(11), 0)

    def test_set_width(self):
        """Tests if set is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle({2, 3, 8}, 7)

    def test_negative_width(self):
        """Tests if a negative number is passed"""
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-9, 5)

    def test_zero_width(self):
        """Tests if zero is passed"""
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 4)

    def test_complex_width(self):
        """Tests if a complex is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(complex(4), 3)

    def test_bool_width(self):
        """Tests if a boolean is passed"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(True, 2)


class TestRectangle_height(unittest.TestCase):
    """Tests the height attribute"""
    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(2, None)

    def test_str_height(self):
        """Tests if string is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(3, 'Cynthia')

    def test_float_height(self):
        """Tests if a float is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(3, 8.1)

    def test_list_height(self):
        """Tests if list is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, [9, 2])

    def test_tuple_height(self):
        """Tests if tuple was passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(3, (9, 5, 1))

    def test_range_height(self):
        """Tests if range is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(5, range(5))

    def test_set_height(self):
        """Tests if set is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(4, {9, 8, 7})

    def test_negative_height(self):
        """Tests if a negative number is passed"""
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(2, -9)

    def test_zero_height(self):
        """Tests if zero is passed"""
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(3, 0)

    def test_complex_height(self):
        """Tests if a complex is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(3, complex(3))

    def test_bool_height(self):
        """Tests if a boolean is passed"""
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(8, True)


class TestRectangle_x(unittest.TestCase):
    """Tests the height attribute"""
    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(2, 3, None, 4)

    def test_str_x(self):
        """Tests if string is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(3, 4, 'Cynthia', 5)

    def test_float_x(self):
        """Tests if a float is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(3, 2, 8.1, 1)

    def test_list_x(self):
        """Tests if list is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 3, [9, 2], 2)

    def test_tuple_x(self):
        """Tests if tuple was passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(3, 3, (9, 5, 1), 6)

    def test_range_x(self):
        """Tests if range is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(5, 4, range(5), 7)

    def test_set_x(self):
        """Tests if set is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(4, 5, {9, 8, 7}, 8)

    def test_negative_x(self):
        """Tests if a negative number is passed"""
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(2, 3, -9, 7)

    def test_complex_x(self):
        """Tests if a complex is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(3, 4, complex(3), 1)

    def test_bool_x(self):
        """Tests if a boolean is passed"""
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(8, 9, True, 9)


class TestRectangle_y(unittest.TestCase):
    """Tests the height attribute"""
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(2, 3, 4, None)

    def test_str_y(self):
        """Tests if string is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(3, 4, 7, 'Cynthia')

    def test_float_y(self):
        """Tests if a float is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(3, 2, 4, 8.1)

    def test_list_y(self):
        """Tests if list is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 3, 10, [9, 2])

    def test_tuple_y(self):
        """Tests if tuple was passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(3, 3, 14, (9, 5, 1))

    def test_range_y(self):
        """Tests if range is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(5, 4, 11, range(5))

    def test_set_y(self):
        """Tests if set is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(4, 5, 15, {9, 8, 7})

    def test_negative_y(self):
        """Tests if a negative number is passed"""
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(2, 3, 3, -9)

    def test_complex_y(self):
        """Tests if a complex is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(3, 4, 5, complex(3))

    def test_bool_y(self):
        """Tests if a boolean is passed"""
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(8, 9, 11, True)


class TestRectangle_area(unittest.TestCase):
    """Unittests the area of a rectangle"""
    def test_area_changed_attributes(self):
        """Tests when attributes are changed"""
        r = Rectangle(2, 3, 0, 0)
        r.width = 5
        r.height = 6
        self.assertEqual(r.area(), 30)

    def test_area(self):
        """Tests the area of rectangle"""
        r = Rectangle(2, 4, 2, 1)
        self.assertEqual(r.area(), 8)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args."""
    def test_update_args_zero(self):
        """Tests when zero arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update()
        self.assertEqual(str(r), '[Rectangle] (12) 2/1 - 4/6')

    def test_update_args_one(self):
        """Tests when one argument is passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6)
        self.assertEqual('[Rectangle] (6) 2/1 - 4/6', str(r))

    def test_update_args_two(self):
        """Tests when two arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6, 3)
        self.assertEqual('[Rectangle] (6) 2/1 - 3/6', str(r))

    def test_update_args_three(self):
        """Tests when three arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6, 3, 9)
        self.assertEqual('[Rectangle] (6) 2/1 - 3/9', str(r))

    def test_update_args_four(self):
        """Tests when four arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6, 3, 9, 7)
        self.assertEqual('[Rectangle] (6) 7/1 - 3/9', str(r))

    def test_update_args_five(self):
        """Tests when five arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6, 3, 9, 7, 10)
        self.assertEqual('[Rectangle] (6) 7/10 - 3/9', str(r))

    def test_update_args_more_than_five(self):
        """Tests when five arguments are passed"""
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(6, 3, 9, 7, 10, 2)
        self.assertEqual('[Rectangle] (6) 7/10 - 3/9', str(r))

    def test_update_args_None_id(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(None)
        updated = "[Rectangle] ({}) 2/1 - 4/6".format(r.id)
        self.assertEqual(updated, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.update(None, 7, 5, 3)
        updated = "[Rectangle] ({}) 3/1 - 7/5".format(r.id)
        self.assertEqual(updated, str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r.update(89, "Cynthia")

    def test_update_args_width_zero(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r.update(89, 2, "Cynthia")

    def test_update_args_height_zero(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(89, 3, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(89, 11, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r.update(89, 2, 5, "Cynthia")

    def test_update_args_x_negative(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r.update(89, 11, 6, -5)

    def test_update_args_invalid_y_type(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r.update(89, 2, 5, 3, "Cynthia")

    def test_update_args_y_negative(self):
        r = Rectangle(4, 6, 2, 1, 12)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r.update(11, 6, 43, 13, -5)


if __name__ == '__main__':
    unittest.main()
