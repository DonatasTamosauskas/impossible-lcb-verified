from typing import List
from collections import Counter


def maximumLength(nums: List[int]) -> int:
    c = Counter(nums)
    best = 1
    if 1 in c:
        best = c[1] if c[1] % 2 == 1 else c[1] - 1
        best = max(best, 1)
    for x in c:
        if x == 1:
            continue
        cur = x
        steps = 0
        while c.get(cur, 0) >= 2 and cur * cur <= 10**9 and (cur * cur) in c:
            cur = cur * cur
            steps += 1
        best = max(best, 2 * steps + 1)
    return best
