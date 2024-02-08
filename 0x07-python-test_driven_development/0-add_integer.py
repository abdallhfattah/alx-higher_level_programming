#!/usr/bin/python3
# 0-add_integer.py
""" Integer addition function defintion"""


def add_integer(a, b=98):
    """ Returns a + b.

    Floats are casted to ints before addition

    Raises:
        TypeError: if a or b are not numbers
    """
    if a is not isinstance(int , float):
        raise TypeError("a must be an integer")
    if b is not isinstance(int , float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)