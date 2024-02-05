#!/usr/bin/python3
"""This module defines function add_attribute"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if its possible.

    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the attribute to add.
        value (any): The value of the attribute.

    Raises:
        TypeError: if the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
