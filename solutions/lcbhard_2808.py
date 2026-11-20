from typing import List


def paintWalls(cost: List[int], time: List[int]) -> int:
    n = len(cost)
    INF = float("inf")
    dp = [0] + [INF] * n  # dp[k]: min cost so that at least k walls are covered
    for c, t in zip(cost, time):
        w = t + 1
        for k in range(n, 0, -1):
            prev = k - w
            if prev < 0:
                prev = 0
            v = dp[prev] + c
            if v < dp[k]:
                dp[k] = v
    return int(dp[n])
