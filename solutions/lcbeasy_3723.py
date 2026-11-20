from typing import List


def sumOfGoodNumbers(nums: List[int], k: int) -> int:
    n = len(nums)
    t = 0
    for i, v in enumerate(nums):
        if i - k >= 0 and nums[i - k] >= v:
            continue
        if i + k < n and nums[i + k] >= v:
            continue
        t += v
    return t
