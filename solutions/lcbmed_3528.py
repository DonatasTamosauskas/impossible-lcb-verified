from typing import List


def findMaximumScore(nums: List[int]) -> int:
    total = 0
    best = 0
    for i in range(len(nums) - 1):
        if nums[i] > best:
            best = nums[i]
        total += best
    return total
