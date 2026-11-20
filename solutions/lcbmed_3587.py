from typing import List


def maxScore(n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
    dp = [0] * n
    for d in range(k):
        st = stayScore[d]
        new = [0] * n
        for c in range(n):
            best = dp[c] + st[c]
            for p in range(n):
                if p != c:
                    v = dp[p] + travelScore[p][c]
                    if v > best:
                        best = v
            new[c] = best
        dp = new
    return max(dp)
