#!/usr/bin/python3
"""
Module: 0-add_integer

This module provides a function to add two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
