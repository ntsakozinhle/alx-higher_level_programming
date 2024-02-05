#!/usr/bin/python3
""" This module defines class MyList """


class MyList(list):
    """Inherits from the list class with an additional public method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
