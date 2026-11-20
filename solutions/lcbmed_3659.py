from typing import List


def countPathsWithXorValue(grid: List[List[int]], k: int) -> int:
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    R = range(16)
    prev = [[0] * 16 for _ in range(n)]
    for i in range(m):
        cur = [None] * n
        for j in range(n):
            g = grid[i][j]
            new = [0] * 16
            if i == 0 and j == 0:
                new[g] = 1
            else:
                up = prev[j] if i else None
                lf = cur[j - 1] if j else None
                for x in R:
                    s = 0
                    if up is not None:
                        s += up[x]
                    if lf is not None:
                        s += lf[x]
                    new[x ^ g] = s % MOD
            cur[j] = new
        prev = cur
    return prev[n - 1][k] % MOD
