from typing import List


def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
    return sum(v for i, v in enumerate(nums) if bin(i).count("1") == k)
