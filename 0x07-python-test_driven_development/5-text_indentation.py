#!/usr/bin/python3
"""
Module: 5-text_indentation

This module provides a function to print a text with 2 new lines after

"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: . , ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("test must be a string")

    line = ""

    for char in text:
        line += char

        if char in ".?:":
            print(line.strip())
            line = ""

    print(line.strip())
