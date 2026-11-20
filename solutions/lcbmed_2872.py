from typing import List


def maxArrayValue(nums: List[int]) -> int:
    cur = nums[-1]
    best = cur
    for v in reversed(nums[:-1]):
        cur = cur + v if v <= cur else v
        if cur > best:
            best = cur
    return best
