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
    total_grid = len(grid)  # the total size of the grid
    total_rows = len(grid[0])  # the total size of the rows

    for row in range(total_grid):
        for cell in range(total_rows):
            # checking if the number is 1 (ground)
            if grid[row][cell] == 1:
                # checking that you don't have 1 on your left
                if cell == 0 or grid[row][cell - 1] == 0:
                    perimeter += 1
                # checking that it doesn't have 1 on its right
                if cell == total_rows - 1 or grid[row][cell + 1] == 0:
                    perimeter += 1
                # verifying that it does not have 1 above it
                if row == 0 or grid[row - 1][cell] == 0:
                    perimeter += 1
                # verifying that it does not have 1 below it
                if row == total_grid - 1 or grid[row + 1][cell] == 0:
                    perimeter += 1

    return perimeter
