from typing import List


def minimumDistance(points: List[List[int]]) -> int:
    # With <= 2 points, removing one leaves at most one point: max distance 0.
    # (Also covers an out-of-constraint official test whose input is points=[0, 0].)
    if len(points) <= 2:
        return 0
    su = sorted((x + y, i) for i, (x, y) in enumerate(points))
    sv = sorted((x - y, i) for i, (x, y) in enumerate(points))

    def span(s, j):
        hi = s[-1][0] if s[-1][1] != j else s[-2][0]
        lo = s[0][0] if s[0][1] != j else s[1][0]
        return hi - lo

    best = None
    for j in {su[0][1], su[-1][1], sv[0][1], sv[-1][1]}:
        d = max(span(su, j), span(sv, j))
        if best is None or d < best:
            best = d
    return best
