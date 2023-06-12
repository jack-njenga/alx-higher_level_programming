#!/usr/bin/python3
"""
BaseGeometry (based on 6-base_geometry.py).
V3
"""


class BaseGeometry():
    """
    BaseGeometry
    V3
    """

    def area(self):
        """
        This area implentation that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this method validates the value
        """
        if isinstance(value, int):
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
