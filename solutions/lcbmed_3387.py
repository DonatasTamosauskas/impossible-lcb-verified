from typing import List


def minOperationsToMakeMedianK(nums: List[int], k: int) -> int:
    a = sorted(nums)
    m = len(a) // 2
    t = 0
    for i in range(m + 1):
        if a[i] > k:
            t += a[i] - k
    for i in range(m, len(a)):
        if a[i] < k:
            t += k - a[i]
    return t
