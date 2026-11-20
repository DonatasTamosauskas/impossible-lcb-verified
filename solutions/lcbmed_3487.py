from typing import List


def maxRemovals(source: str, pattern: str, targetIndices: List[int]) -> int:
    m = len(pattern)
    NEG = -10**9
    tset = set(targetIndices)
    dp = [NEG] * (m + 1)
    dp[0] = 0
    for i, c in enumerate(source):
        r = 1 if i in tset else 0
        for j in range(m - 1, -1, -1):
            v = dp[j + 1] + r
            if c == pattern[j] and dp[j] > v:
                v = dp[j]
            dp[j + 1] = v
        dp[0] += r
    return dp[m]
