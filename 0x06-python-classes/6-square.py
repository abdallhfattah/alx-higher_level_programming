#!/usr/bin/python3
"""Square model"""


class Square:
    """Defines square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: length of a square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    def area(self):
        return self.__size ** 2

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
            or len(value) != 2
                or not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, s):
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
