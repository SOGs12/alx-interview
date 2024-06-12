#!/usr/bin/python3
"""
This module contains the rotate_2d_matrix function definition.
"""

def rotate_2d_matrix(matrix: list[list[int]]) -> None:
    """
    Rotates an n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.
    """
    n = len(matrix)

    # Transpose the matrix in place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in place
    for i in range(n):
        matrix[i].reverse()
