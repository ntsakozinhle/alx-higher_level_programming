#!/usr/bin/python3
"""This modules defines a Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square
        __position (tuple): Private attribute representing the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): the position of the square. Defaults to (0, 0)
        """
        self.size = size
        self.position =position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square

        Args:
            value (int): the new size of square

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value (tuple): the new position of the square

        Raises:
            TypeError: if the value is not a tuple of the 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and eturns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters and the specified position"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
