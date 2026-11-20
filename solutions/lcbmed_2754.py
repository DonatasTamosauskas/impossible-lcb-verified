from typing import List


def maxStrength(nums: List[int]) -> int:
    best = None
    n = len(nums)
    for m in range(1, 1 << n):
        p = 1
        for i in range(n):
            if m >> i & 1:
                p *= nums[i]
        if best is None or p > best:
            best = p
    return best
