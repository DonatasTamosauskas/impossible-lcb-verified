from typing import List


def countWays(nums: List[int]) -> int:
    a = sorted(nums)
    n = len(a)
    r = 0
    for k in range(n + 1):
        if (k == 0 or a[k - 1] < k) and (k == n or a[k] > k):
            r += 1
    return r
