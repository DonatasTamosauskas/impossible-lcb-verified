from collections import deque


def minimumOperationsToMakeEqual(x: int, y: int) -> int:
    limit = 2 * max(x, y) + 20
    dist = {x: 0}
    q = deque([x])
    while q:
        u = q.popleft()
        if u == y:
            return dist[u]
        nxt = [u - 1, u + 1]
        if u % 11 == 0:
            nxt.append(u // 11)
        if u % 5 == 0:
            nxt.append(u // 5)
        for v in nxt:
            if 0 < v <= limit and v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return abs(x - y)
