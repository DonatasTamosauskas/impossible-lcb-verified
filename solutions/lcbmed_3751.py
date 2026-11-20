from typing import List


def maxFrequency(nums: List[int], k: int) -> int:
    total = nums.count(k)
    best = 0
    for v in set(nums):
        if v == k:
            continue
        cur = 0
        for x in nums:
            if x == v:
                cur += 1
            elif x == k:
                cur -= 1
            if cur < 0:
                cur = 0
            if cur > best:
                best = cur
    return total + best
