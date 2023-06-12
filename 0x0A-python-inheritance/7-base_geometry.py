#!/usr/bin/python3

"""
BaseGeometry (based on 6-base_geometry.py).
V3
"""
Base = __import__("6-base_geometry").BaseGeometry


class BaseGeometry(Base):
    """
    BaseGeometry
    V3
    """

    def area(self):
        """
        raises an exception if area is not implement
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this methon validates the value
        """
        if value.__class__ == int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
