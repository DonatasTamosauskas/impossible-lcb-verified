from typing import List
from collections import defaultdict


def longestEqualSubarray(nums: List[int], k: int) -> int:
    pos = defaultdict(list)
    for i, v in enumerate(nums):
        pos[v].append(i)
    best = 0
    for p in pos.values():
        l = 0
        for r in range(len(p)):
            while p[r] - p[l] - (r - l) > k:
                l += 1
            best = max(best, r - l + 1)
    return best
