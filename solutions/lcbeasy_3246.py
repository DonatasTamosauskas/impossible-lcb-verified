from typing import List


def hasTrailingZeros(nums: List[int]) -> bool:
    return sum(1 for x in nums if x % 2 == 0) >= 2
