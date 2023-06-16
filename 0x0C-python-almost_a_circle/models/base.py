#!/usr/bin/python3
"""
Base Class
"""


class Base:
    """
    Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Keeps count on id

        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
            __nb_objects += 1
