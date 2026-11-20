from typing import List
from bisect import bisect_left


def _pals():
    res = []
    for L in range(1, 10):
        h = (L + 1) // 2
        for x in range(10 ** (h - 1), 10 ** h):
            s = str(x)
            t = s + (s[::-1] if L % 2 == 0 else s[-2::-1])
            res.append(int(t))
    return res


_P = _pals()


def minimumCost(nums: List[int]) -> int:
    a = sorted(nums)
    n = len(a)
    med = a[n // 2]
    i = bisect_left(_P, med)
    cands = _P[max(0, i - 1):i + 1]
    return min(sum(abs(v - y) for v in a) for y in cands)
