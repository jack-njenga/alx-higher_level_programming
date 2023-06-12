#!/usr/bin/python3
"""
add_attribute: adds a new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object if it’s possible:

    Args:
        obj (object): the object to add attribute
        attr (str): the attribute to add the object to
        value (int / str / ...): the value to set the attribute to
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
