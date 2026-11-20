from math import gcd
from typing import List


def maxLength(nums: List[int]) -> int:
    best = 0
    n = len(nums)
    for i in range(n):
        p, g, l = 1, 0, 1
        for j in range(i, n):
            x = nums[j]
            p *= x
            g = gcd(g, x)
            l = l * x // gcd(l, x)
            if p == l * g:
                best = max(best, j - i + 1)
    return best
