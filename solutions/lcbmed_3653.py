from typing import List


def maxSubarraySum(nums: List[int], k: int) -> int:
    INF = float("inf")
    best = [INF] * k
    best[0] = 0
    p = 0
    ans = -INF
    for i, x in enumerate(nums, 1):
        p += x
        r = i % k
        if best[r] != INF and p - best[r] > ans:
            ans = p - best[r]
        if p < best[r]:
            best[r] = p
    return ans
