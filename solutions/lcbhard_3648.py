from typing import List


def _corner(g: List[List[int]], n: int) -> int:
    # child starting at (0, n-1), moving down one row per step, staying strictly above the diagonal
    NEG = float("-inf")
    prev = [NEG] * (n + 1)
    prev[n - 1] = g[0][n - 1]
    for i in range(1, n - 1):
        cur = [NEG] * (n + 1)
        row = g[i]
        lo = max(i + 1, n - 1 - i)
        for j in range(lo, n):
            a = prev[j - 1]
            b = prev[j]
            c = prev[j + 1]
            m = a if a > b else b
            if c > m:
                m = c
            cur[j] = m + row[j]
        prev = cur
    return prev[n - 1]


def maxCollectedFruits(fruits: List[List[int]]) -> int:
    n = len(fruits)
    diag = sum(fruits[i][i] for i in range(n))
    if n == 1:
        return diag
    t = [list(col) for col in zip(*fruits)]
    return int(diag + _corner(fruits, n) + _corner(t, n))
