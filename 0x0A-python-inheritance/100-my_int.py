#!/usr/bin/python3
"""
This is a rebel integer implementation
"""

class MyInt(int):
    """
    This is a rebel integer implementation
    """

    def __init__(self, num):
        """
        Initialization
        """
        self.__num = num

    def __eq__(self, value):
        """
        Overrides the == operator
        """
        return (super().__ne__(value))

    def __ne__(self, value):
        """
        Overrides the != operator
        """
        return (super().__eq__(value))


