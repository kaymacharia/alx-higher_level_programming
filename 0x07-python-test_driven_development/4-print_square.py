#!/usr/bin/python3
"""
This module is composed by a function that prints a square with the character #
"""


def print_square(size):
    """ A function that generates a square using the "#" character when printed.
    Args:
        size: size of the square printed
    Returns:
        No return
    Raises:
        
TypeError occurs when the value assigned to "size" is not an integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
