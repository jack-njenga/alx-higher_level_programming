#!/usr/bin/python3

"""
This function adds 2 integers and returns the sum.
"""


def add_integer(a, b=98):
    """
    adds up thw integers.

    Args:
        a (int): first integer
        b (int): second integer (default: 98)

    Returns:
        int: sum of the two integers

    >>> add_integer(-5, 10)
    5

    >>> add_integer(5.5, 2)
    7

    >>> add_integer(10)
    108

    >>> add_integer('2', 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 10, in add_integer
    TypeError: a must be an integer

    >>> add_integer(2, '3')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 12, in add_integer
    TypeError: b must be an integer

    >>> add_integer(True, False)
    1
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)
