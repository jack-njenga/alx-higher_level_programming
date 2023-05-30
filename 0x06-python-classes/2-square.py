#!/usr/bin/python3

"""
Square V2
defines a square with size
"""


class Square:
    """
    Square
    """
    def __init__(self, size=0):
        """
        size must be >= 0 and an int.
        Args:
            size (int): size of the square
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
