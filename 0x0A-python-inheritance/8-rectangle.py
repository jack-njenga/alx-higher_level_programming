#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry (7-base_geometry.py).
V4
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle
    V4
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        Args:
            width (int) - the width of the rectangle
            height (int) - the height of the rectangle
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
