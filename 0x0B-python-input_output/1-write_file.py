#!/usr/bin/python3
"""Module for writing a string to a text file (UTF8) and returning the number
of characters written."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
    written.

    Args:
        filename (str): The name of the text file to write to. Default is an
        empty string.
        text (str): The string to write to the file. Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(tect)
    return nb_characters


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.text", "This School is so cool!\n")
    print(nb_characters)
