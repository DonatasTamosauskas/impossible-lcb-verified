import heapq
from typing import List


def minTimeToReach(moveTime: List[List[int]]) -> int:
    n, m = len(moveTime), len(moveTime[0])
    INF = float("inf")
    dist = [[INF] * m for _ in range(n)]
    dist[0][0] = 0
    h = [(0, 0, 0)]
    while h:
        d, i, j = heapq.heappop(h)
        if d > dist[i][j]:
            continue
        if i == n - 1 and j == m - 1:
            return d
        for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= a < n and 0 <= b < m:
                nd = max(d, moveTime[a][b]) + 1
                if nd < dist[a][b]:
                    dist[a][b] = nd
                    heapq.heappush(h, (nd, a, b))
    return dist[n - 1][m - 1]
