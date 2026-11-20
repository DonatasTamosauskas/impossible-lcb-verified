from typing import List


def isGood(nums: List[int]) -> bool:
    n = max(nums)
    return sorted(nums) == list(range(1, n + 1)) + [n]
