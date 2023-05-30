#!/usr/bin/python3
"""
Square V3
upgrade based on V2
"""


class Square:
    """
    Square
    returns the current square area.
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

    def area(self):
        """
        returns the current square area
        """

        return (self.__size * self.__size)
