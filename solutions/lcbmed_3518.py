from typing import List


def maxScore(a: List[int], b: List[int]) -> int:
    NEG = float('-inf')
    dp = [0] + [NEG] * 4
    for x in b:
        for j in range(4, 0, -1):
            if dp[j - 1] != NEG:
                c = dp[j - 1] + a[j - 1] * x
                if c > dp[j]:
                    dp[j] = c
    return int(dp[4])
