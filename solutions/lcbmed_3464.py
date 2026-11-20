from typing import List


def maximumTotalCost(nums: List[int]) -> int:
    NEG = float("-inf")
    a = nums[0]
    b = NEG
    for x in nums[1:]:
        a, b = max(a, b) + x, a - x
    return int(max(a, b))
