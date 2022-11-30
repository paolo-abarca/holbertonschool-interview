#!/usr/bin/python3
"""
function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
"""
from math import factorial


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
        for i in range(n):
            for j in range(i + 1):
                number = factorial(i)//(factorial(j)*factorial(i-j))
                result.append(number)
            final.append(result)
            result = []

    return final
