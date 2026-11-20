from typing import List


def lenOfVDiagonal(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    # Directions in clockwise order: down-right, down-left, up-left, up-right.
    dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def chain_lengths(dr, dc):
        # f[i*m+j] = length of alternating 2/0 chain starting at (i, j) going (dr, dc).
        f = [0] * (n * m)
        rows = range(n - 1, -1, -1) if dr == 1 else range(n)
        for i in rows:
            row = grid[i]
            base = i * m
            ni = i + dr
            if 0 <= ni < n:
                nrow = grid[ni]
                nbase = ni * m
                for j in range(m):
                    v = row[j]
                    if v == 1:
                        continue
                    nj = j + dc
                    if 0 <= nj < m and nrow[nj] == 2 - v:
                        f[base + j] = f[nbase + nj] + 1
                    else:
                        f[base + j] = 1
            else:
                for j in range(m):
                    if row[j] != 1:
                        f[base + j] = 1
        return f

    F = [chain_lengths(dr, dc) for dr, dc in dirs]

    best = 0
    for i in range(n):
        row = grid[i]
        for j in range(m):
            if row[j] != 1:
                continue
            if best < 1:
                best = 1
            for d in range(4):
                dr, dc = dirs[d]
                f2 = F[(d + 1) & 3]
                ci = i + dr
                cj = j + dc
                t = 1
                expected = 2
                while 0 <= ci < n and 0 <= cj < m and grid[ci][cj] == expected:
                    cand = t + f2[ci * m + cj]
                    if cand > best:
                        best = cand
                    t += 1
                    expected = 2 - expected
                    ci += dr
                    cj += dc
    return best
