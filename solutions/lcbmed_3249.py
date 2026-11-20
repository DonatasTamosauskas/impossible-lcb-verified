from typing import List


def minOperations(nums: List[int], k: int) -> int:
    x = k
    for v in nums:
        x ^= v
    return bin(x).count("1")
