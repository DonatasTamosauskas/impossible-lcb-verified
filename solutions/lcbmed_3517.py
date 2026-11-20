from typing import List


def shortestDistanceAfterQueries(n: int, queries: List[List[int]]) -> List[int]:
    adj = [[i + 1] if i < n - 1 else [] for i in range(n)]
    res = []
    for u, v in queries:
        adj[u].append(v)
        dist = [-1] * n
        dist[0] = 0
        q = [0]
        for x in q:
            for y in adj[x]:
                if dist[y] < 0:
                    dist[y] = dist[x] + 1
                    q.append(y)
        res.append(dist[n - 1])
    return res
