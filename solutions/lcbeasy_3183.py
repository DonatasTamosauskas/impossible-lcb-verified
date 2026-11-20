from typing import List


def findKOr(nums: List[int], k: int) -> int:
    res = 0
    for b in range(32):
        if sum((x >> b) & 1 for x in nums) >= k:
            res |= 1 << b
    return res
