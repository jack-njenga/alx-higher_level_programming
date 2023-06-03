#!/usr/bin/python3

"""
This function prints a square with '#' charactes.
"""


def print_square(size):
    """
    Prints a square with '#' charactes.

    Args:
        size (int): size length of the square

    Doctests:
    >>> print_square(5)
    #####
    #####
    #####
    #####
    #####
    >>> print_square(5.5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 14, in print_square
    TypeError: size must be an integer
    >>> print_square(-5.5)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 12, in print_square
    TypeError: size must be an integer
    >>> print_square(100 - 100)
    >>> print_square(1)
    #
    """
    error_1 = "size must be an integer"
    error_2 = "size must be >= 0"
    if (isinstance(size, float) and size < 0):
        raise TypeError(error_1)
    if not isinstance(size, int):
        raise TypeError(error_1)
    if size < 0:
        raise ValueError(error_2)
    for i in range(size):
        print("#" * size)
