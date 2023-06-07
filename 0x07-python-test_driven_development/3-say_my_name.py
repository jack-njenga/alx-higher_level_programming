#!/usr/bin/python3
"""
This function prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name

    Doctests:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Lucy", "W")
    My name is Lucy W
    >>> say_my_name(123, "Smith")
    Traceback (most recent call last):
    ...
    TypeError: first_name must be a string
    >>> say_my_name("John", 456)
    Traceback (most recent call last):
    ...
    TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {}".format(first_name, last_name))
