from typing import List


def maximumBeauty(nums: List[int], k: int) -> int:
    a = sorted(nums)
    best = 0
    l = 0
    for r in range(len(a)):
        while a[r] - a[l] > 2 * k:
            l += 1
        best = max(best, r - l + 1)
    return best
