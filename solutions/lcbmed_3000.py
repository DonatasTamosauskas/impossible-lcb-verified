from bisect import bisect_left, insort
from typing import List


def minAbsoluteDifference(nums: List[int], x: int) -> int:
    best = float("inf")
    seen = []
    for j in range(x, len(nums)):
        insort(seen, nums[j - x])
        v = nums[j]
        p = bisect_left(seen, v)
        if p < len(seen):
            best = min(best, seen[p] - v)
        if p > 0:
            best = min(best, v - seen[p - 1])
        if best == 0:
            break
    return int(best)
