#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class that defines a square with a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initialize the square with a private instance attribute: size.
        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
