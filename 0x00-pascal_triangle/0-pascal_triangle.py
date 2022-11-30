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
        return result

    else:
        for i in range(n):
            number = str(11 ** i)

            if len(number) != 1:
                for n in number:
                    result.append(n)
            else:
                result.append(number)

            final.append(result)
            result = []

    return final
