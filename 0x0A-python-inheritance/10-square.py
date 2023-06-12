#!/usr/bin/python3
"""
Square
V6
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square
    V6
    """
    def __init__(self, size):
        """
        Initialization
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
