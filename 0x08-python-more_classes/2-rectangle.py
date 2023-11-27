#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
"""The "Rectangle" class characterizes a rectangle using the following features:
Private instance attributes: "width" (an integer) and "height" (an integer).
Option to create instances with customizable width and height.
Public instance methods: "area(self)" to calculate the area of the rectangle and "perimeter(self)" to determine its perimeter.
"""

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the value of the width property. """
        return self.__width

    @property
    def height(self):
        """ Retrieve the value of the height property. """
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the value of the width property. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Set the value of the height property. """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
