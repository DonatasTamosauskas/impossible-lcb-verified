from typing import List


def minimumCost(nums: List[int]) -> int:
    a, b = sorted(nums[1:])[:2]
    return nums[0] + a + b
