from typing import List


def maximumJumps(nums: List[int], target: int) -> int:
    n = len(nums)
    NEG = -1
    dp = [NEG] * n
    dp[0] = 0
    for j in range(1, n):
        best = NEG
        for i in range(j):
            if dp[i] >= 0 and abs(nums[j] - nums[i]) <= target and dp[i] + 1 > best:
                best = dp[i] + 1
        dp[j] = best
    return dp[-1]
