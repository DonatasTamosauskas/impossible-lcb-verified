from bisect import bisect_left
from typing import List


def maximumWeight(intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    order = sorted(range(n), key=lambda i: intervals[i][1])
    rs = [intervals[i][1] for i in order]
    # p[t]: number of sorted intervals ending strictly before interval t starts
    p = [bisect_left(rs, intervals[order[t]][0]) for t in range(n)]

    # State key: (-total_weight, sorted index list); smaller is better.
    empty = (0, [])
    prev = [empty] * (n + 1)  # layer j-1: best using at most j-1 intervals among first i
    best = empty
    for _ in range(4):
        cur = [empty] * (n + 1)
        for t in range(n):
            idx = order[t]
            w = intervals[idx][2]
            base = prev[p[t]]
            cand = (base[0] - w, sorted(base[1] + [idx]))
            c = cur[t]
            cur[t + 1] = cand if cand < c else c
        prev = cur
        if cur[n] < best:
            best = cur[n]
    return list(best[1])
