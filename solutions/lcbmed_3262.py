from typing import List


def largestPerimeter(nums: List[int]) -> int:
    a = sorted(nums)
    total = sum(a)
    for i in range(len(a) - 1, 1, -1):
        total -= a[i]
        if total > a[i]:
            return total + a[i]
    return -1
