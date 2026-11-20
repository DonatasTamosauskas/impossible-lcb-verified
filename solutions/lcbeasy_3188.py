from typing import List


def findChampion(grid: List[List[int]]) -> int:
    n = len(grid)
    for a in range(n):
        if all(grid[b][a] == 0 for b in range(n)):
            return a
    return -1
