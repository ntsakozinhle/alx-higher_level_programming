#!/usr/bin/python3
"""This module defines a Magic class."""
import math


class MagicClass:
    """
    A class that represents a magical circle with radius.

    Attributes:
        __radius (float or int): the radius of the magical circle.

    Methods:
        __init__(self, radius=0): Initializes a new MagicClass instance.
        area(self): Calculates and returns the area of the magical circle
        circumference(self): Calculates and returns the circumference of
        the magical circle
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (float or int, optional): The radius of the magical circle.
            Defaults to 0.

        Raises:
            TypeError: if the radius is not a number (float or int).
        """
        self.radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

        def area(self):
            """
            Calculates and returns the area of the magical circle.

            Returns:
                float: the area of the magical circle.
            """
            return self.__radius ** 2 * math.pi

        def circumference(self):
            """
            Calculates and returns the circumference of the magical circle.

            Returns:
                float: the circumference of the magical circle.
            """
            return 2 * math.pi * self.__radius
