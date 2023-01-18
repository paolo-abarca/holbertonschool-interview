#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Method that modify matrix must be edited in-place
    """
    # we copy the original matrix to edit with the correct data
    copy_matrix = [[j for j in i] for i in matrix]

    # we use the copy to get the values
    i = 0
    for matrix_row in copy_matrix[::-1]:
        j = 0
        for matrix_column in matrix_row:
            # iterate the matrix in reverse so that it edits from top to bottom
            matrix[j][i] = matrix_column
            j += 1
        i += 1
