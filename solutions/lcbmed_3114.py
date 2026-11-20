from typing import List


def maximumSumOfHeights(maxHeights: List[int]) -> int:
    n = len(maxHeights)
    best = 0
    for p in range(n):
        t = maxHeights[p]
        m = t
        for i in range(p - 1, -1, -1):
            m = min(m, maxHeights[i])
            t += m
        m = maxHeights[p]
        for i in range(p + 1, n):
            m = min(m, maxHeights[i])
            t += m
        best = max(best, t)
    return best
