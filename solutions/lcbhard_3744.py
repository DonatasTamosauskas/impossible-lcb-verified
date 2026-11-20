from typing import List


def _prefix_steps(x: int) -> int:
    # Sum over v in [1, x] of the number of base-4 digits of v.
    total = 0
    lo = 1
    k = 1
    while lo <= x:
        hi = lo * 4 - 1
        if hi > x:
            hi = x
        total += (hi - lo + 1) * k
        lo *= 4
        k += 1
    return total


def _steps(x: int) -> int:
    s = 0
    while x:
        x //= 4
        s += 1
    return s


def minOperations(queries: List[List[int]]) -> int:
    res = 0
    for l, r in queries:
        s = _prefix_steps(r) - _prefix_steps(l - 1)
        res += max((s + 1) // 2, _steps(r))
    return res
