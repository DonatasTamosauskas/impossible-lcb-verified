from typing import List


def maxScore(points: List[int], m: int) -> int:
    n = len(points)

    def check(low: int) -> bool:
        rem = m
        pre = 0
        for i in range(n):
            p = points[i]
            k = (low + p - 1) // p - pre
            if i == n - 1 and k <= 0:
                break
            if k < 1:
                k = 1
            rem -= 2 * k - 1
            if rem < 0:
                return False
            pre = k - 1
        return True

    lo, hi = 0, (m + 1) // 2 * min(points) + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    return lo
