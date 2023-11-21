#!/usr/bin/python3
""" The Square class defines a square and includes a
private instance attribute named 'size'. It allows
instantiation with an optional 'size' parameter, with
the condition that the provided 'size' must be of integer type.
"""


class Square:
    """Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
