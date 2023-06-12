#!/usr/bin/python3

"""
returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj (object) - object
        a_class (object) - obj...
    >>> class MyClass: pass
    >>> class Myclass_2: pass
    >>> obj1 = MyClass()
    >>> obj2 = Myclass_2()
    >>> is_same_class(obj1, MyClass)
    True
    >>> is_same_class(obj1, Myclass_2)
    False
    >>> is_same_class(obj2, Myclass_2)
    True
    """
    return type(obj) is a_class
