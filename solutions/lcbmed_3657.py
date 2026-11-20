from typing import List


def _ok(iv):
    iv.sort()
    groups = 0
    end = -1
    for s, e in iv:
        if s >= end:
            groups += 1
        if e > end:
            end = e
    return groups >= 3


def checkValidCuts(n: int, rectangles: List[List[int]]) -> bool:
    return _ok([(r[0], r[2]) for r in rectangles]) or _ok([(r[1], r[3]) for r in rectangles])
