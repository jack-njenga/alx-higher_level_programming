#!/usr/bin/python3
"""

"""
from models.base import Base



class Rectangle(Base):
    """
    This is the Rectangle class that inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): x co-ordinate of the rectangle's position default: 0)
            y (int): y-coordinate of the rectangle's position (default: 0)
            id (int): ID value for the rectangle (default: None).
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an int")

        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an int")

        if type(x) == int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an int")

        if type(y) == int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an int")

        super().__init__(id)

    @property
    def width(self):
        """
        get current width
        """
        return self.__width

    @width.setter
    def width(self, new):
        """
        set new width
        """
        self.__width = new

    @property
    def height(self):
        """
        get current height
        """
        return self.__height

    @height.setter
    def height(self, new):
        """
        set new height
        """
        self.__height = new

    @property
    def x(self):
        """
        get x co-ordinates
        """
        return self.__x
    @x.setter
    def x(self, new):
        """
        set new x co-ordinates
        """
        self.__x = new

    @property
    def y(self):
        """
        get y co-ordinates
        """
        return self.__y

    @y.setter
    def y(self, new):
        """
        set new y co-ordinates
        """
        self.__y = new
