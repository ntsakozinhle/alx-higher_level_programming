#!/usr/bin/python3
""" This module defines class MyInt """


class MyInt(int):
    """A class representing a rebel integer."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
