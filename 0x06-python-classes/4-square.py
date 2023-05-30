#!/usr/bin/python3

"""
Square V4
upgrade based on V3
"""


class Square:
    """
    Square

    """
    def __init__(self, size=0):
        """
        Args:
            size (int): size of the square.
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        for retriving the size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area of the square.
        """
        ans = self.__size**2
        return (ans)
