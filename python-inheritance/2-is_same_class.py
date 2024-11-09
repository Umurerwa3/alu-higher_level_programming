#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj: object to check type.
        a_class: type to check against.

    Returns:
        bool: True if obj is an instance of a_class, else False.
    """
    return type(obj) is a_class  # Using 'is' for strict type comparison
