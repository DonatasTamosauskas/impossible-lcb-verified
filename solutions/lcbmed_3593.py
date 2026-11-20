from math import gcd
from typing import List


def maxScore(nums: List[int]) -> int:
    def f(a):
        if not a:
            return 0
        g = 0
        l = 1
        for x in a:
            g = gcd(g, x)
            l = l * x // gcd(l, x)
        return g * l
    best = f(nums)
    for i in range(len(nums)):
        best = max(best, f(nums[:i] + nums[i + 1:]))
    return best
