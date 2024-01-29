#!/usr/bin/python3
"""
Module: 2-matrix_divided

This module provides a function to divide all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide all elements of the matrix.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                    if each row of the matrix does not have the same size,
                    or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    if not all(
                isinstance(row, list) and all(isinstance(el, (int, float))
    for el in row) for row in matrix
            ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
