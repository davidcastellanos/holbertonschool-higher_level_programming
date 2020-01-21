#!/usr/bin/python3
"""Module implementing BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """BaseGeometry class to extend"""

    def area(self):
        """Function to compute area of self"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Function to validate value is an int"""

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
