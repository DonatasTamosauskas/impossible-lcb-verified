from typing import List
from collections import deque


def _diameter(edges: List[List[int]]) -> int:
    n = len(edges) + 1
    if n == 1:
        return 0
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def bfs(src):
        dist = [-1] * n
        dist[src] = 0
        q = deque([src])
        far = src
        while q:
            u = q.popleft()
            du = dist[u]
            if du > dist[far]:
                far = u
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = du + 1
                    q.append(v)
        return far, dist[far]

    a, _ = bfs(0)
    _, d = bfs(a)
    return d


def minimumDiameterAfterMerge(edges1: List[List[int]], edges2: List[List[int]]) -> int:
    d1 = _diameter(edges1)
    d2 = _diameter(edges2)
    return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
