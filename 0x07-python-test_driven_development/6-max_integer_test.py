#!/usr/bin/python3
"""Module used for determining the highest integer within a given list.
"""


def max_integer(list=[]):
    """A function that identifies and retrieves the largest integer from a list of integers. If the list is empty, the function returns None.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
