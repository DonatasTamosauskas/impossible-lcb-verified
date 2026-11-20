from typing import List


def minChanges(nums: List[int], k: int) -> int:
    n = len(nums)
    m = n // 2
    eq = [0] * (k + 2)
    diff = [0] * (k + 3)
    for i in range(m):
        a, b = nums[i], nums[n - 1 - i]
        d = abs(a - b)
        mx = max(a, b, k - a, k - b)
        eq[d] += 1
        diff[0] += 1
        diff[mx + 1] -= 1
    best = 2 * m
    cur = 0
    for x in range(k + 1):
        cur += diff[x]
        best = min(best, 2 * m - cur - eq[x])
    return best
