#!/usr/bin/python3

"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle that inherits from Base.
         Attributes:
            __width: Width of the Rectangle
            __height: Height of the rectangle
            __x: Coordinates of rectangle
            __y: coordinates of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter"""
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Defines area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the character # to the stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print() for y in range(self.y)]
        for row in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for column in range(self.width)]
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
            Attributes:
                id: 1st attribute
                width: 2nd attribute
                height: 3rd attribute
                x: 4th attribute
                y: 5th attribute
        """
        if args or len(args) != 0:
            argument = 0
            for arg in args:
                if argument == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif argument == 1:
                    self.width = arg
                elif argument == 2:
                    self.height = arg
                elif argument == 3:
                    self.x = arg
                elif argument == 4:
                    self.y = arg
                argument += 1
        elif kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    def __str__(self):
        """Returns a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
