from typing import List


def maxSum(grid: List[List[int]], limits: List[int], k: int) -> int:
    vals = []
    for row, lim in zip(grid, limits):
        if lim > 0:
            vals.extend(sorted(row, reverse=True)[:lim])
    vals.sort(reverse=True)
    return sum(vals[:k])
