from typing import List


def numberOfRightTriangles(grid: List[List[int]]) -> int:
    rows = [sum(r) for r in grid]
    cols = [sum(c) for c in zip(*grid)]
    t = 0
    for i, r in enumerate(grid):
        for j, v in enumerate(r):
            if v:
                t += (rows[i] - 1) * (cols[j] - 1)
    return t
