from typing import List
from collections import Counter


def maximumTotalDamage(power: List[int]) -> int:
    cnt = Counter(power)
    keys = sorted(cnt)
    n = len(keys)
    dp = [0] * (n + 1)
    j = 0
    for i in range(n):
        v = keys[i]
        while keys[j] < v - 2:
            j += 1
        dp[i + 1] = max(dp[i], dp[j] + v * cnt[v])
    return dp[n]
