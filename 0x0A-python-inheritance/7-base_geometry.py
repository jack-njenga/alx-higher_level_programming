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
        this method validates the value
        """
        if type(value) == int:
            if value <= 0:
                raise ValueError("{:s} must be greater than 0".format(name))
            else:
                pass
        else:
            raise TypeError("{:s} must be an integer".format(name))
