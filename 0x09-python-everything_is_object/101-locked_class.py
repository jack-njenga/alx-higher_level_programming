#!/usr/bin/python3

"""
LockedClass - prevents the user from dynamically
creating new instance attributes, except if the new
instance attribute is called
"""


class LockedClass:
    """
    LockedClass
    """
    __slots__ = ["first_name"]
