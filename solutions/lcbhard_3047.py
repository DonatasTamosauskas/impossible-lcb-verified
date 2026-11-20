from typing import List


def maximumSum(nums: List[int]) -> int:
    # Indices i, j have a perfect-square product iff they share the same
    # square-free part. Each group is {k * m^2} for a square-free k; summing
    # over every k (square-free or not) only adds subsets of valid groups.
    n = len(nums)
    best = 0
    for k in range(1, n + 1):
        total = 0
        m = 1
        while k * m * m <= n:
            total += nums[k * m * m - 1]
            m += 1
        if total > best:
            best = total
    return best
