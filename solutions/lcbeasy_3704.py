from typing import List


def countPartitions(nums: List[int]) -> int:
    return len(nums) - 1 if sum(nums) % 2 == 0 else 0
