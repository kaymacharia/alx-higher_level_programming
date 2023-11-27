#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """
   The "Rectangle" class is structured with the following features:

Private instance attributes: "width" (an integer) and "height" (an integer).
It allows instantiation with optional width and height parameters.
Includes public instance methods: "area(self)" for computing the rectangle's area and "perimeter(self)" for determining its perimeter.
Customized behavior for the print() and str() methods to display the rectangle using the "#" character.
The repr() method returns a string representation to recreate a new instance using eval().
It contains a deconstructor method that executes 'Bye rectangle...' when invoked.
Additionally, there are public class attributes: "number_of_instances" to track the count of instances created and "print_symbol" for the string representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor method """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter width property """
        return self.__width

    @property
    def height(self):
        """ getter height property """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter height property """
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

    def __str__(self):
        """ Return string to print rectangle with # """
        if self.width == 0 or self.height == 0:
            return ''
        to_print = ''
        for col in range(self.height):
            for row in range(self.width):
                to_print += str(self.print_symbol)
            if col != self.height - 1:
                to_print += '\n'
        return to_print

    def __repr__(self):
        """ Return a string representation of the rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Deconstructor method """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
