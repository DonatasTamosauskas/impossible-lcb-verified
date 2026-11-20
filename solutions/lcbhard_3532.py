from typing import List


def timeTaken(edges: List[List[int]]) -> List[int]:
    n = len(edges) + 1
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    w = [1 if i & 1 else 2 for i in range(n)]

    parent = [-1] * n
    order = []
    seen = [False] * n
    seen[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                parent[v] = u
                stack.append(v)

    best1 = [0] * n
    best2 = [0] * n
    bestc = [-1] * n
    for u in reversed(order):
        p = parent[u]
        if p >= 0:
            val = best1[u] + w[u]
            if val > best1[p]:
                best2[p] = best1[p]
                best1[p] = val
                bestc[p] = u
            elif val > best2[p]:
                best2[p] = val

    up = [0] * n
    for u in order:
        p = parent[u]
        if p >= 0:
            sib = best2[p] if bestc[p] == u else best1[p]
            up[u] = w[p] + max(up[p], sib)

    return [max(best1[i], up[i]) for i in range(n)]
