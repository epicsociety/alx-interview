#!/usr/bin/python3
""" Island perimeter """
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if j == 1:
                if grid[i][j-1] == 0:
                    perimeter += 1
                if i - 1 < 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j + 1 < columns and grid[i][j+1] == 0:
                    perimeter += 1
                if i + 1 < rows and grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
