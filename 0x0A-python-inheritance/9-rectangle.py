#!/usr/bin/python3
""" This module defines class BaseGeometry and Rectangle """


class BaseGeometry:
    """ An class representing a base geometry. """

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value for being an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description as a string."""
        return "[Rectangle] {}/{}"/format(self.__width, self.__height)
