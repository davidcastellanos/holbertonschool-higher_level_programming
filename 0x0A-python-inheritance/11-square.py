#!/usr/bin/python3
"""Module implementing Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""


class Square(__import__('9-rectangle').Rectangle):
    """Class to represent a Square as a subclass of Rectangle"""

    def __init__(self, size):
        """Initialize new Square object"""

        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Compute area of square"""

        return self.__size * self.__size

    def __str__(self):
        """Return a formatted string to be printed"""

        return '[Square] {0}/{0}'.format(self.__size)
