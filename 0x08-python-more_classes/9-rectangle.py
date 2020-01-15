#!/usr/bin/python3
"""Module Number 10 containing Rectangle class"""


class Rectangle:
    """rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.
        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """`height` function attribute.
        Returns: `height` attribute value.
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
        Returns: `width` attribute value.
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
        """Method - instance to compute Rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Method to compute perimeter length of Rectangle instance.
        Returns: 2 * (w + h) if both `width` and `height` > 0, else 0.
        """
        return 2*(self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
 
        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width + '\n'
        return rect[:-1]

    def __repr__(self):
 
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
     
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
 
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
 
        return cls(size, size)
