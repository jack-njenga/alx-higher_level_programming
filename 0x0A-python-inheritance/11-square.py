#!/usr/bin/python3
"""
Rectangle
V7
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Rectangle
    V7
    """
    def __init__(self, size):
        """
        Initialization
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        This is str() implemntaion for printing
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
