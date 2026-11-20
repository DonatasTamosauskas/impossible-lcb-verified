from typing import List


def minimumRightShifts(nums: List[int]) -> int:
    n = len(nums)
    s = sorted(nums)
    for k in range(n):
        if nums[n - k:] + nums[:n - k] == s:
            return k
    return -1
