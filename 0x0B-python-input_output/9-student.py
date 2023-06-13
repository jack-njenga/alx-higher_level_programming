#!/usr/bin/python3
"""
File: 9-student.py
Description: This Module contains Student class
Author: Jack Njenga
Version: 1.0
Date Created: 13 June 2023
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization
        """
        self.fist_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrives te dictionary repr.. of Student class
        """
        return self.__dict__
