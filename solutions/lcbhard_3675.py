from typing import List


def maximizeSumOfWeights(edges: List[List[int]], k: int) -> int:
    n = len(edges) + 1
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    parent = [-1] * n
    pw = [0] * n
    order = []
    seen = [False] * n
    seen[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not seen[v]:
                seen[v] = True
                parent[v] = u
                pw[v] = w
                stack.append(v)
    dp0 = [0] * n  # parent edge removed: up to k child edges
    dp1 = [0] * n  # parent edge kept: up to k-1 child edges
    for u in reversed(order):
        base = 0
        gains = []
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            base += dp0[v]
            g = dp1[v] + w - dp0[v]
            if g > 0:
                gains.append(g)
        gains.sort(reverse=True)
        s_k1 = sum(gains[:k - 1]) if k - 1 > 0 else 0
        s_k = s_k1 + (gains[k - 1] if len(gains) >= k else 0)
        dp0[u] = base + s_k
        dp1[u] = base + s_k1
    return dp0[0]
