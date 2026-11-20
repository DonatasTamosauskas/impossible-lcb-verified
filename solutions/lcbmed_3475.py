from typing import List


def minOperations(nums: List[int]) -> int:
    a = list(nums)
    n = len(a)
    ops = 0
    for i in range(n - 2):
        if a[i] == 0:
            a[i] = 1
            a[i + 1] ^= 1
            a[i + 2] ^= 1
            ops += 1
    if a[n - 2] == 1 and a[n - 1] == 1:
        return ops
    return -1
