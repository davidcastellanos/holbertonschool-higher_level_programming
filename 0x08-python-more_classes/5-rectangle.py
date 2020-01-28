#!/usr/bin/python3
"""class Number 6 for rectangle project"""


class Rectangle:
    """rectangle object"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Getter function for `height` attribute.
        Returns: value of `height` attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """`height` attribute function.
        Args:
            value (int): `height` value.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """`width` attribute function.
        Returns: value of `width` attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """`width` attribute function.
        Args:
            value (int): `width` value.
        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):

        return self.width * self.height

    def perimeter(self):
  
        return 2*(self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
 
        rect = ""
        for i in range(self.height):
            rect += '#'*self.width + '\n'
        return rect[:-1]

    def __repr__(self):
 
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):

        print("Bye rectangle...")