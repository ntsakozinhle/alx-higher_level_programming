#!/usr/bin/python3
"""Module for defining a Student class."""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a student instance.

        Args:
            attrs (list, optional): A list of strings specifying which
            attribute to recive. If None, all attributes will be retrived.
            Default is None.

        Returns:
            dict: a dictionary containing the attribute of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
