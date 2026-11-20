from typing import List


def maxSelectedElements(nums: List[int]) -> int:
    dp = {}
    best = 0
    for x in sorted(nums):
        dp[x + 1] = dp.get(x, 0) + 1
        dp[x] = dp.get(x - 1, 0) + 1
        a = dp[x + 1]
        b = dp[x]
        if a > best:
            best = a
        if b > best:
            best = b
    return best
