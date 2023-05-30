#!/usr/bin/python

"""
Square implementation V2
addition of private size instace attribute to V1
"""


class Square:
    """
    Square implementation
    """
    def __init__(self, size):
        """
        Initialize new square.
        Args:
            self (self): self identity
            size (int): Size of the square
        """
        self.__size = size
