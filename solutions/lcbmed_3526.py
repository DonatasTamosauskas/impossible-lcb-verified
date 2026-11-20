from typing import List


def minFlips(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    r = 0
    for row in grid:
        for j in range(n // 2):
            if row[j] != row[n - 1 - j]:
                r += 1
    c = 0
    for i in range(m // 2):
        t, u = grid[i], grid[m - 1 - i]
        for j in range(n):
            if t[j] != u[j]:
                c += 1
    return min(r, c)
