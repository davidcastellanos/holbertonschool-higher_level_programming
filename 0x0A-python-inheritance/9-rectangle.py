#!/usr/bin/python3
"""Module to extend BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Class to represent a rectangle"""

    def __init__(self, width, height):
        """Initialize new rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):


        return self.__width * self.__height

    def __str__(self):
        """Return a formatted string to be printed"""

        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
