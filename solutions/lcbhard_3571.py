from bisect import bisect_left
from typing import List


def _lis_strict(points):
    # Longest chain strictly increasing in both coordinates.
    points.sort(key=lambda p: (p[0], -p[1]))
    tails = []
    for _, y in points:
        pos = bisect_left(tails, y)
        if pos == len(tails):
            tails.append(y)
        else:
            tails[pos] = y
    return len(tails)


def maxPathLength(coordinates: List[List[int]], k: int) -> int:
    xk, yk = coordinates[k]
    lower = [(x, y) for x, y in coordinates if x < xk and y < yk]
    upper = [(x, y) for x, y in coordinates if x > xk and y > yk]
    return 1 + _lis_strict(lower) + _lis_strict(upper)
