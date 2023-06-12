#!/usr/bin/python3
"""
MyList that inherits from list.
"""


class MyList(list):
    """
    Inherits from:
        list: Built-in Python list class
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
