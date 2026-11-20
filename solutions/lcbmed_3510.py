from typing import List


def maximumTotalSum(maximumHeight: List[int]) -> int:
    cur = 10**18
    total = 0
    for m in sorted(maximumHeight, reverse=True):
        h = min(m, cur - 1)
        if h < 1:
            return -1
        total += h
        cur = h
    return total
