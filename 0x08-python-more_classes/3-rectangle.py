#!/usr/bin/python3

"""
Rectangle V10
"""


class Rectangle:
    """
    Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialization
        """
        self.__width = width
        self.__height = height
        self.add_to_class()

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
            raise TypeError("width must be an integer")
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
        heigth setter
        """
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
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

    def __str__(self):
        """
        returns a string to be printed
        """
        ret = ""
        if (self.area() == 0):
            return ret
        for i in range(self.__height):
            ret += str(self.print_symbol) * self.__width
            if i < self.height - 1:
                ret += "\n"

        return ret
