import heapq
from typing import List


def resultsArray(queries: List[List[int]], k: int) -> List[int]:
    h = []
    out = []
    for x, y in queries:
        d = abs(x) + abs(y)
        if len(h) < k:
            heapq.heappush(h, -d)
        elif d < -h[0]:
            heapq.heapreplace(h, -d)
        out.append(-h[0] if len(h) == k else -1)
    return out
