from typing import List


def maxRectangleArea(points: List[List[int]]) -> int:
    pts = set(map(tuple, points))
    best = -1
    for (x1, y1) in pts:
        for (x2, y2) in pts:
            if x1 < x2 and y1 < y2 and (x1, y2) in pts and (x2, y1) in pts:
                ok = True
                for (x, y) in pts:
                    if x1 <= x <= x2 and y1 <= y <= y2 and (x, y) not in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                        ok = False
                        break
                if ok:
                    best = max(best, (x2 - x1) * (y2 - y1))
    return best
