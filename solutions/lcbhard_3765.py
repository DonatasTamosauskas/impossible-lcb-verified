from typing import List


def minimumCost(nums: List[int], cost: List[int], k: int) -> int:
    n = len(nums)
    pn = [0] * (n + 1)
    pc = [0] * (n + 1)
    for i in range(n):
        pn[i + 1] = pn[i] + nums[i]
        pc[i + 1] = pc[i] + cost[i]
    total = pc[n]
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[0] = 0
    for r in range(1, n + 1):
        a = pn[r]
        b = pc[r]
        best = INF
        for l in range(r):
            pl = pc[l]
            v = dp[l] + a * (b - pl) + k * (total - pl)
            if v < best:
                best = v
        dp[r] = best
    return dp[n]
