#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): Private attribute representing the size
        of the square
    """

    def __init__(self, size=0):
        """Initializes a new Square instace

        Args:
            size (float or int, optional): the size of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float or int): The new size of the square

        Raises:
            TypeError: if the value is not a number (float or int)
            ValueErrorr: if the value is less than 0
        """
        if not is instance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the equality operator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Defines the inequality operator"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Defines the less than operator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Defines the less than or equal to operator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """Defines the greater than operator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Defines the greater than or equal to operator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
