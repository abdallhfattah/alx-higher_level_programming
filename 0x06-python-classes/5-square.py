#!/usr/bin/python3
"""Square model"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a square.
        """
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="\n" if j == self.__size - 1 and i != j else "")
            print()
