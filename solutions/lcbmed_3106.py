from typing import List


def lengthOfLongestSubsequence(nums: List[int], target: int) -> int:
    NEG = -10**9
    dp = [NEG] * (target + 1)
    dp[0] = 0
    for x in nums:
        for s in range(target, x - 1, -1):
            v = dp[s - x] + 1
            if v > dp[s]:
                dp[s] = v
    return dp[target] if dp[target] > 0 else -1
