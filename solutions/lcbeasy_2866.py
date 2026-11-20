from typing import List


def longestAlternatingSubarray(nums: List[int], threshold: int) -> int:
    best = 0
    n = len(nums)
    for l in range(n):
        if nums[l] % 2 != 0 or nums[l] > threshold:
            continue
        r = l
        while r + 1 < n and nums[r + 1] <= threshold and nums[r + 1] % 2 != nums[r] % 2:
            r += 1
        best = max(best, r - l + 1)
    return best
