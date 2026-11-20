from typing import List


def minCost(n: int, cost: List[List[int]]) -> int:
    states = [(a, b) for a in range(3) for b in range(3) if a != b]
    m = n // 2
    dp = {s: cost[0][s[0]] + cost[n - 1][s[1]] for s in states}
    for i in range(1, m):
        r = n - 1 - i
        nd = {}
        for (c, d) in states:
            best = min(v for (a, b), v in dp.items() if a != c and b != d)
            nd[(c, d)] = best + cost[i][c] + cost[r][d]
        dp = nd
    return min(dp.values())
