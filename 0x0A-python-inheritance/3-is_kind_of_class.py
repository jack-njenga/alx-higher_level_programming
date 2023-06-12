#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the
bject is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj (object) - obj...
        a_class (object) = obj...
    >>> class MyBaseClass: pass
    >>> class Myclass(MyBaseClass): pass
    >>> class Class_2: pass
    >>> obj1 = Myclass()
    >>> obj2 = Class_2()
    >>> is_kind_of_class(obj1, Myclass)
    True
    >>> is_kind_of_class(obj1, Class_2)
    False
    """
    return isinstance(obj, a_class)
