from typing import List


def numberOfSubmatrices(grid: List[List[str]]) -> int:
    n = len(grid[0])
    xs = [0] * n
    ys = [0] * n
    res = 0
    for row in grid:
        rx = ry = 0
        for j in range(n):
            c = row[j]
            if c == 'X':
                rx += 1
            elif c == 'Y':
                ry += 1
            xs[j] = (xs[j - 1] if False else 0) + xs[j] + rx
            ys[j] = ys[j] + ry
            if xs[j] == ys[j] and xs[j] > 0:
                res += 1
    return res
