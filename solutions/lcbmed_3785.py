from typing import List


def countArrays(original: List[int], bounds: List[List[int]]) -> int:
    lo, hi = -10**18, 10**18
    base = original[0]
    for i, (u, v) in enumerate(bounds):
        d = original[i] - base
        lo = max(lo, u - d)
        hi = min(hi, v - d)
    return max(0, hi - lo + 1)
