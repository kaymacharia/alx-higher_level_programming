#!/usr/bin/python3
""" The Square class defines a square shape utilizing private
instance attributes like 'size' and 'position'. It incorporates
getter and setter methods and can be created with an optional size
parameter, ensuring it's an integer value. It includes public instance
methods: 'area(self)' and 'my_print(self)'. Moreover, it permits comparison
with other instances.
"""


class Square:
    """Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """Size getter"""
    @property
    def size(self):
        return self.__size

    """Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """returns the current square area"""
    def area(self):
        return self.__size ** 2

    """True if self is less or equal than other"""
    def __le__(self, other):
        return self.area() <= other.area()

    """True if self is less than other"""
    def __lt__(self, other):
        return self.area() < other.area()

    """True if self is equal than other"""
    def __eq__(self, other):
        return self.area() == other.area()

    """True if self is greater or equal than other"""
    def __ge__(self, other):
        return self.area() >= other.area()

    """True if self is greater than other"""
    def __gt__(self, other):
        return self.area() > other.area()

    """True if self is not equeal other"""
    def __ne__(self, other):
        return self.area() != other.area()
