#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class that defines a square with a private instance attribute: size.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a private instance attribute: size.

        Args:
            size (int): The size of the square, default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size