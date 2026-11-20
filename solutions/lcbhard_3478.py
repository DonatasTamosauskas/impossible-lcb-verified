from typing import List
from collections import deque


def canReachCorner(xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
    X, Y = xCorner, yCorner
    n = len(circles)

    def contains(x, y, r, px, py):
        return (x - px) ** 2 + (y - py) ** 2 <= r * r

    def touches_left_or_top(x, y, r):
        # left edge x = 0, 0 <= y <= Y ; top edge y = Y, 0 <= x <= X
        return (abs(x) <= r and 0 <= y <= Y) or (abs(y - Y) <= r and 0 <= x <= X)

    def touches_right_or_bottom(x, y, r):
        # right edge x = X, 0 <= y <= Y ; bottom edge y = 0, 0 <= x <= X
        return (abs(x - X) <= r and 0 <= y <= Y) or (abs(y) <= r and 0 <= x <= X)

    for x, y, r in circles:
        if contains(x, y, r, 0, 0) or contains(x, y, r, X, Y):
            return False

    seen = [False] * n
    for s in range(n):
        if seen[s]:
            continue
        x, y, r = circles[s]
        if not touches_left_or_top(x, y, r):
            continue
        seen[s] = True
        dq = deque([s])
        while dq:
            i = dq.popleft()
            x1, y1, r1 = circles[i]
            if touches_right_or_bottom(x1, y1, r1):
                return False
            for j in range(n):
                if seen[j]:
                    continue
                x2, y2, r2 = circles[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 + r2) ** 2:
                    continue
                # A point common to both disks (dividing the centres in ratio r1:r2) must lie
                # inside the rectangle for the two disks to be connected within it.
                if x1 * r2 + x2 * r1 < (r1 + r2) * X and y1 * r2 + y2 * r1 < (r1 + r2) * Y:
                    seen[j] = True
                    dq.append(j)
    return True
