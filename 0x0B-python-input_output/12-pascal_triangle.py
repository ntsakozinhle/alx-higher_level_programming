#!/usr/bin/python3
"""Module defineing Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the pascals triangle of n

    Args:
        n (int): Number of rows to generate in the Pascal's triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
