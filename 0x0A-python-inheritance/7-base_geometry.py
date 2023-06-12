#!/usr/bin/python3

"""
BaseGeometry (based on 6-base_geometry.py).
V3
"""


class BaseGeometry(object):
    """
    BaseGeometry
    V3
    """

    def area(self):
        """
        raises an exception if area is not implement
        """
        raise Exception("area() is not implemented")

    def interger_validator(self, name, value):
        """
        this methon validates the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
