from typing import List


def alternatingSubarray(nums: List[int]) -> int:
    best = -1
    n = len(nums)
    for i in range(n - 1):
        if nums[i + 1] - nums[i] != 1:
            continue
        j = i + 1
        while j + 1 < n and nums[j + 1] == nums[j - 1]:
            j += 1
        best = max(best, j - i + 1)
    return best
