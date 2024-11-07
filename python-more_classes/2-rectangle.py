#!/usr/bin/python3
"""Defines a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """calculates area of a rectangle 


        return:
            int: area.
        """
        return self.__width * self.__height
    def perimeter(self):
        """calculates perimeter of a rectangle


        returns:
            int: perimeter.
        """
        if self.__height == 0 or self.__width == 0
        return perimeter == 0
        else:
        return 2*(self.__height + self.__width)
