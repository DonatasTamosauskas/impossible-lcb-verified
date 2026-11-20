from typing import List


def minimumPairRemoval(nums: List[int]) -> int:
    a = list(nums)
    ops = 0
    while any(a[i] > a[i + 1] for i in range(len(a) - 1)):
        m = min(range(len(a) - 1), key=lambda i: a[i] + a[i + 1])
        a[m:m + 2] = [a[m] + a[m + 1]]
        ops += 1
    return ops
