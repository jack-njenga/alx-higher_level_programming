#!/usr/bin/python3

"""
This function returns the list of available attributes and
methods of an object.
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of
    an object.
    Args:
        obj (object) - object
    Returns:
        Returns a list object

    >>> lookup(object)[:] == ['__setattr__', '__sizeof__']
    False
    >>> lookup(object)[-1] == ['__str__', '__subclasshook__', '__fbref__']
    False
    """
    return dir(obj)
