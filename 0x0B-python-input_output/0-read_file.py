#!/usr/bin/python3
"""Module for reading text file and printing to stdout"""


def read_file(filename=""):
    """
    Read a text filee (UTF8) and print its content to stdout.

    Args:
        filename (str): The name of the text file to read. Default is an empty
        string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file()
