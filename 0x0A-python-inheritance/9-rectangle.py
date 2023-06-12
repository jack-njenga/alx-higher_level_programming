#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry (7-base_geometry.py)
V5
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    V5
    """
    def __init__(self, width, height):
        """
        Initialization
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This is the area implentetion
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        this is the str() implementation for printing
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
