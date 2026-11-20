from typing import List


def _count_at_most(nums: List[int], m: int, size: int) -> int:
    cnt = [0] * size
    distinct = 0
    left = 0
    total = 0
    for right, x in enumerate(nums):
        if cnt[x] == 0:
            distinct += 1
        cnt[x] += 1
        while distinct > m:
            y = nums[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                distinct -= 1
            left += 1
        total += right - left + 1
    return total


def medianOfUniquenessArray(nums: List[int]) -> int:
    n = len(nums)
    total = n * (n + 1) // 2
    need = (total + 1) // 2
    size = max(nums) + 1
    lo, hi = 1, len(set(nums))
    while lo < hi:
        mid = (lo + hi) // 2
        if _count_at_most(nums, mid, size) >= need:
            hi = mid
        else:
            lo = mid + 1
    return lo
