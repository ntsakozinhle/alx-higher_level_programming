#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instace.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): the new size of the square.

        Raises:
            TypeError: if the value is not an Integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
