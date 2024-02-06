#!/usr/bin/python3
"""Square model"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a square.
        """
        if (size >= 0):
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2
