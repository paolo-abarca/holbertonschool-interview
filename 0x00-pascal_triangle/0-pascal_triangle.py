#!/usr/bin/python3
"""
function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    result = []
    final = []

    if n <= 0:
        return []

    else:
        for i in range(1, n + 1):
            c = 1
            for j in range(1, i + 1):
                result.append(c)
                c = c * (i - j) // j

            final.append(result)
            result = []

    return final
