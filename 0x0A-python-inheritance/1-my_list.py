#!/usr/bin/python3
"""
MyList that inherits from list.
"""


class MyList(list):
    """
    Inherits fr*m  list the Built-in Python list class
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        Args:
            self (object) - object
        """
        sorted_list = sorted(self)
        print(sorted_list)
