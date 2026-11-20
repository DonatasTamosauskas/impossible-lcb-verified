from typing import List
from collections import defaultdict


def minimumSeconds(nums: List[int]) -> int:
    n = len(nums)
    pos = defaultdict(list)
    for i, v in enumerate(nums):
        pos[v].append(i)
    best = n
    for p in pos.values():
        gap = p[0] + n - p[-1]
        for a, b in zip(p, p[1:]):
            if b - a > gap:
                gap = b - a
        best = min(best, gap // 2)
    return best
