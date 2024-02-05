#!/usr/bin/python3
""" This module defines function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or of the object is an
    instance of a class that inherited from, the specified class; otherwise
    False.

    Args:
        obj (object): the object to check.
        a_class (class): the class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses, False
        otherwise.
    """
    return isinstance(obj, a_class)
