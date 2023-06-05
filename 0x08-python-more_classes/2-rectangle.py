#!/usr/bin/python3

"""
Rectangle V3
"""


class Rectangle:
    """
    Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        initialization
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrives the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrives the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        ans = (self.__width * self.__height)
        return ans

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        ans = ((self.__width * 2) + (self.__height * 2))
        return ans
