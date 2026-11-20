from typing import List


def findMinimumTime(strength: List[int], K: int) -> int:
    n = len(strength)
    INF = float("inf")
    dp = [INF] * (1 << n)
    dp[0] = 0
    for m in range(1 << n):
        if dp[m] == INF:
            continue
        x = 1 + K * bin(m).count("1")
        for i in range(n):
            if not m >> i & 1:
                t = dp[m] + (strength[i] + x - 1) // x
                nm = m | 1 << i
                if t < dp[nm]:
                    dp[nm] = t
    return dp[(1 << n) - 1]
