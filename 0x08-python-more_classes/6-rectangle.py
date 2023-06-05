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
    def heigth(self, value):
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
        returns a tring to be peinted
        """
        ret = ""
        if (self.area() == 0):
            return ret
        for i in range(self.__height):
            ret += str(self.print_symbol) * self.__width
            if i < self.height - 1:
                ret += "\n"

        return ret

    def __repr__(self):
        """
        """
        ans = "Rectangle({}, {})".format(self.__width, self.__height)
        return ans

    @classmethod
    def __del__(cls):
        """
        """
        print("Bye rectangle...")
        cls.number_of_instances -= 1

    @classmethod
    def add_to_class(cls):
        """
        adds a new instance
        """
        cls.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return cls(size, size)
