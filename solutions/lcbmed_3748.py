from typing import List


def sortMatrix(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    res = [row[:] for row in grid]
    for d in range(-(n - 1), n):
        cells = [(i, i - d) for i in range(n) if 0 <= i - d < n]
        vals = sorted(grid[i][j] for i, j in cells)
        if d >= 0:
            vals.reverse()
        for (i, j), v in zip(cells, vals):
            res[i][j] = v
    return res
