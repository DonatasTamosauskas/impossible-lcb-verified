from bisect import bisect_right
from typing import List


def maximumCoins(coins: List[List[int]], k: int) -> int:
    segs = sorted(coins)
    ls = [s[0] for s in segs]
    cum = [0]
    for l, r, c in segs:
        cum.append(cum[-1] + (r - l + 1) * c)

    def F(x):
        if x <= 0:
            return 0
        i = bisect_right(ls, x) - 1
        if i < 0:
            return 0
        l, r, c = segs[i]
        return cum[i] + (min(x, r) - l + 1) * c

    best = 0
    for l, r, c in segs:
        best = max(best, F(l + k - 1) - F(l - 1), F(r) - F(r - k))
    return best
