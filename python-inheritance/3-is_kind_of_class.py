#!/usr/bin/python3
"""Defines a function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of or if the object is,
    an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: object to check type.
        a_class: type to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, else False.
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)
