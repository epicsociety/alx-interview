#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    return a list of lists
    pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        new_row = [1]
        for j in range(1, i):
            new_row.append(triangle[i-1][j - 1] + triangle[i-1][j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
