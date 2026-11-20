from bisect import bisect_left
from typing import List


def _occ(s, p):
    r = []
    i = s.find(p)
    while i != -1:
        r.append(i)
        i = s.find(p, i + 1)
    return r


def beautifulIndices(s: str, a: str, b: str, k: int) -> List[int]:
    A = _occ(s, a)
    B = _occ(s, b)
    res = []
    for i in A:
        j = bisect_left(B, i - k)
        if j < len(B) and B[j] <= i + k:
            res.append(i)
    return res
