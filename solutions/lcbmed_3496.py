from math import isqrt
from typing import List


def minNumberOfSeconds(mountainHeight: int, workerTimes: List[int]) -> int:
    ws = sorted(workerTimes)
    mn = ws[0]
    lo, hi = 1, mn * mountainHeight * (mountainHeight + 1) // 2
    while lo < hi:
        t = (lo + hi) // 2
        tot = 0
        for w in ws:
            q = t // w
            if q == 0:
                break
            # largest x with x(x+1)/2 <= q
            tot += (isqrt(8 * q + 1) - 1) // 2
            if tot >= mountainHeight:
                break
        if tot >= mountainHeight:
            hi = t
        else:
            lo = t + 1
    return lo
