from typing import List


def minimumSum(nums: List[int]) -> int:
    n = len(nums)
    best = -1
    for j in range(1, n - 1):
        l = min(nums[:j])
        r = min(nums[j + 1:])
        if l < nums[j] and r < nums[j]:
            s = l + nums[j] + r
            if best == -1 or s < best:
                best = s
    return best
