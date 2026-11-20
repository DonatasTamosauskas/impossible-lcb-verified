from typing import List


def minimumOperations(nums: List[int]) -> int:
    return sum(1 for x in nums if x % 3)
