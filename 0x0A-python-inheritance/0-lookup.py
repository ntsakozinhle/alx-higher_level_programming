#!/usr/bin/python3
"""This module defines lookup function"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object for which attributes and methods are to be
        looked up

    Returns:
        list: a list containing the names of attributes and methods of the
        object
    """
    return dir(obj)
