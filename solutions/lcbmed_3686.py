from typing import List


def beautifulSplits(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and nums[z[i]] == nums[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    zm = 0
    for i in range(1, n):
        if z[i] >= i:
            zm |= 1 << i
    masks = {}
    for i, v in enumerate(nums):
        masks[v] = masks.get(v, 0) | (1 << i)
    vals = list(masks.values())
    total = 0
    for d in range(1, n - 1):
        E = 0
        for m in vals:
            E |= m & (m >> d)
        A = E
        ln = 1
        while ln * 2 <= d:
            A &= A >> ln
            ln *= 2
        if ln < d:
            A &= A >> (d - ln)
        i2max = n - 2 * d
        ok2 = 0
        if i2max >= 1:
            ok2 = A & (((1 << (i2max + 1)) - 1) ^ 1)
        top = min(d, n - 1 - d)
        ok1 = zm & (((1 << (top + 1)) - 1) ^ 1)
        total += bin(ok1 | ok2).count("1")
    return total
