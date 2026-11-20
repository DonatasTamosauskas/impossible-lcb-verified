from typing import List


def minimumArea(grid: List[List[int]]) -> int:
    r0 = c0 = 10**9
    r1 = c1 = -1
    for i, row in enumerate(grid):
        if 1 in row:
            if i < r0:
                r0 = i
            r1 = i
            a = row.index(1)
            b = len(row) - 1 - row[::-1].index(1)
            if a < c0:
                c0 = a
            if b > c1:
                c1 = b
    return (r1 - r0 + 1) * (c1 - c0 + 1)
