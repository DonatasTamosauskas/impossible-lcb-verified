from collections import Counter
from typing import List


def getLargestOutlier(nums: List[int]) -> int:
    total = sum(nums)
    cnt = Counter(nums)
    best = None
    for o in cnt:
        rem = total - o
        if rem % 2:
            continue
        sm = rem // 2
        need = cnt.get(sm, 0)
        if sm == o:
            need -= 1
        if need >= 1:
            if best is None or o > best:
                best = o
    return best
