from typing import List


def maxScore(grid: List[List[int]]) -> int:
    rows_of = {}
    for r, row in enumerate(grid):
        for v in set(row):
            rows_of.setdefault(v, []).append(r)
    m = len(grid)
    full = 1 << m
    neg = -1
    dp = [neg] * full
    dp[0] = 0
    for v in sorted(rows_of):
        rows = rows_of[v]
        new = dp[:]
        for mask in range(full):
            base = dp[mask]
            if base < 0:
                continue
            for r in rows:
                bit = 1 << r
                if not mask & bit:
                    nm = mask | bit
                    if base + v > new[nm]:
                        new[nm] = base + v
        dp = new
    return max(dp)
