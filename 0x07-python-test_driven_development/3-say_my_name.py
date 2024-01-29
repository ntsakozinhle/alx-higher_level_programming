#!/usr/bin/python3
"""
Module: 3-say_my_name

This module provides a function to print a person's name.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the person's first and last name.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person
        (default is an empty string)

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
