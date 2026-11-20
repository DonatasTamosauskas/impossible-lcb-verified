from typing import List


def maxSum(nums: List[int]) -> int:
    pos = {x for x in nums if x > 0}
    return sum(pos) if pos else max(nums)
