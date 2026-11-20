from typing import List


def minOperations(nums: List[int], k: int) -> int:
    return sum(1 for x in nums if x < k)
