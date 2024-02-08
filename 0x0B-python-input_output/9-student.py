#!/usr/bin/python3
"""Module for defining a Student class."""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of a student instance.

        Returns:
            dict: a dictionary containing the attribute of the Student instance.
        """
        return {
                'first_name': self.first_name, 
                'last_name': self.last_name,
                'age': self.age
        }
