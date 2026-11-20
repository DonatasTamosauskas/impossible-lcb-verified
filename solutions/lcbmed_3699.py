from typing import List
from math import gcd
from collections import defaultdict


def numberOfSubsequences(nums: List[int]) -> int:
    n = len(nums)
    cnt = defaultdict(int)
    ans = 0
    for r in range(4, n - 2):
        q = r - 2
        b = nums[q]
        for p in range(0, q - 1):
            a = nums[p]
            g = gcd(a, b)
            cnt[(a // g) * 1001 + b // g] += 1
        c = nums[r]
        for s in range(r + 2, n):
            d = nums[s]
            g = gcd(d, c)
            ans += cnt.get((d // g) * 1001 + c // g, 0)
    return ans
