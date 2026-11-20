from typing import List


def maxSubarrays(n: int, conflictingPairs: List[List[int]]) -> int:
    byB = [[] for _ in range(n + 1)]
    for a, b in conflictingPairs:
        if a > b:
            a, b = b, a
        byB[b].append(a)
    max1 = 0
    max2 = 0
    base = 0
    gain = [0] * (n + 1)
    for r in range(1, n + 1):
        for a in byB[r]:
            if a > max1:
                max2 = max1
                max1 = a
            elif a > max2:
                max2 = a
        base += r - max1
        if max1 > 0:
            gain[max1] += max1 - max2
    return base + max(gain)
