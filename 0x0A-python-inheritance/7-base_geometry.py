#!/usr/bin/python3
""" This module defines class BaseGeometry """


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
