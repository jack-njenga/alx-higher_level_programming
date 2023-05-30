#!/usr/bin/python3

"""
Square implementation V1
addition of private size instace attribute to V0
"""


class Square:
    """
    Square implementation
    """
    def __init__(self, size):
        """
        Initialization
        Args:
            size (int): Size of the square
        """
        self.__size = size
