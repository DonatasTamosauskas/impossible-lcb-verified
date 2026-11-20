from typing import List


def maxDistance(side: int, points: List[List[int]], k: int) -> int:
    P = 4 * side
    pos = []
    for x, y in points:
        if x == 0:
            t = y
        elif y == side:
            t = side + x
        elif x == side:
            t = 3 * side - y
        else:
            t = 4 * side - x
        pos.append(t)
    pos.sort()
    n = len(pos)

    def feasible(d: int) -> bool:
        # nxt[i] = first index j > i with pos[j] >= pos[i] + d, or n
        nxt = [n] * (n + 1)
        j = 0
        for i in range(n):
            target = pos[i] + d
            if j < i + 1:
                j = i + 1
            while j < n and pos[j] < target:
                j += 1
            nxt[i] = j
        nxt[n] = n
        limit = P - d
        # only starts whose position allows k points with gaps >= d before wrap
        starts = [i for i in range(n) if pos[i] + (k - 1) * d <= pos[-1]]
        if not starts:
            return False
        cur = starts[:]
        for _ in range(k - 1):
            cur = [nxt[c] for c in cur]
        for s, c in zip(starts, cur):
            if c < n and pos[c] - pos[s] <= limit:
                return True
        return False

    lo, hi = 1, side
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
