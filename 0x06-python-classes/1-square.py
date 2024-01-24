#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
