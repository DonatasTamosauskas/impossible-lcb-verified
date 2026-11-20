from typing import List


def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    d = [0] * (n + 1)
    for l, r in queries:
        d[l] += 1
        d[r + 1] -= 1
    c = 0
    for i in range(n):
        c += d[i]
        if nums[i] > c:
            return False
    return True
