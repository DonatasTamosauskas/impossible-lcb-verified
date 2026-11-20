from typing import List


def maximizeTheProfit(n: int, offers: List[List[int]]) -> int:
    by_end = [[] for _ in range(n)]
    for s, e, g in offers:
        by_end[e].append((s, g))
    dp = [0] * (n + 1)
    for i in range(n):
        best = dp[i]
        for s, g in by_end[i]:
            v = dp[s] + g
            if v > best:
                best = v
        dp[i + 1] = best
    return dp[n]
