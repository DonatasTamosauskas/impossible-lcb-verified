from collections import Counter
from typing import List


def minGroupsForValidAssignment(nums: List[int]) -> int:
    cnts = list(Counter(nums).values())
    k = min(cnts)
    for s in range(k, 0, -1):
        total = 0
        ok = True
        for c in cnts:
            g = -(-c // (s + 1))
            if g * s > c:
                ok = False
                break
            total += g
        if ok:
            return total
    return len(nums)
