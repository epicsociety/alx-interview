#!/usr/bin/python3
""" Rotate a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """ rotate it 90 degrees clockwise in place"""
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
