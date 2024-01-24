#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Represents a Square.

    Attributes:
        __size (int): Private attribute representing the size of the square.
    """


    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
