#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Method that returns the perimeter
    of the island described in grid
    """
    perimeter = 0
    # traversing the grid rows
    for row in range(len(grid)):
        for number in range(len(grid[row])):
            # checking if the number is 1 (ground)
            if grid[row][number] == 1:
                # checking that you don't have 1 on your left
                if grid[row][number - 1] == 0:
                    perimeter += 1
                # checking that it doesn't have 1 on its right
                if grid[row][number + 1] == 0:
                    perimeter += 1
                # verifying that it does not have 1 above it
                if grid[row - 1][number] == 0:
                    perimeter += 1
                # verifying that it does not have 1 below it
                if grid[row + 1][number] == 0:
                    perimeter += 1

    return perimeter
