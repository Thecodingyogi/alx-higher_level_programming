#!/usr/bin/python3

"""Defines a Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assigns attributes
            Arg:
                id: 1st argument
                size: 2nd arguments
                x: 3rd argument
                y: 4th argument
        """
        if args and len(args) != 0:
            argument = 0
            for arg in args:
                if argument == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argument == 1:
                    self.size = arg
                elif argument == 2:
                    self.x = arg
                elif argument == 3:
                    self.y = arg
                argument += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """Returns the string of the Square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
