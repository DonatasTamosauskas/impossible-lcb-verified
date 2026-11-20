from typing import List


def maximumLength(nums: List[int], k: int) -> int:
    n = len(nums)
    # dp[i][j]: longest good subsequence ending at i using j changes
    dp = [[1] * (k + 1) for _ in range(n)]
    best = 1
    for i in range(n):
        di = dp[i]
        for p in range(i):
            dp_p = dp[p]
            if nums[p] == nums[i]:
                for j in range(k + 1):
                    v = dp_p[j] + 1
                    if v > di[j]:
                        di[j] = v
            else:
                for j in range(1, k + 1):
                    v = dp_p[j - 1] + 1
                    if v > di[j]:
                        di[j] = v
        best = max(best, max(di))
    return best
