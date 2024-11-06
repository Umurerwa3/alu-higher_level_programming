#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
