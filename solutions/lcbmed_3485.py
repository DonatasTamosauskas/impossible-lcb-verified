from typing import List


def maxPossibleScore(start: List[int], d: int) -> int:
    s = sorted(start)

    def ok(g):
        cur = s[0]
        for v in s[1:]:
            cur = max(v, cur + g)
            if cur > v + d:
                return False
        return True

    lo, hi = 0, (s[-1] + d - s[0]) // (len(s) - 1)
    while lo < hi:
        m = (lo + hi + 1) // 2
        if ok(m):
            lo = m
        else:
            hi = m - 1
    return lo
