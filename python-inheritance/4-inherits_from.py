#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited,
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: object to check type.
        a_class: type to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
