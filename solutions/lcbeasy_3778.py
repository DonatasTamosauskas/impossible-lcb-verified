from typing import List


def transformArray(nums: List[int]) -> List[int]:
    odd = sum(x % 2 for x in nums)
    return [0] * (len(nums) - odd) + [1] * odd
