from collections import deque
from typing import List


def findSafeWalk(grid: List[List[int]], health: int) -> bool:
    m, n = len(grid), len(grid[0])
    INF = float("inf")
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    dq = deque([(0, 0)])
    while dq:
        i, j = dq.popleft()
        d = dist[i][j]
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < m and 0 <= y < n:
                nd = d + grid[x][y]
                if nd < dist[x][y]:
                    dist[x][y] = nd
                    if grid[x][y]:
                        dq.append((x, y))
                    else:
                        dq.appendleft((x, y))
    return health - dist[m - 1][n - 1] >= 1
