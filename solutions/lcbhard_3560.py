from typing import List
from collections import deque


def _bfs(sx: int, sy: int) -> List[int]:
    N = 50
    dist = [-1] * (N * N)
    dist[sx * N + sy] = 0
    dq = deque([(sx, sy)])
    moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
    while dq:
        x, y = dq.popleft()
        d = dist[x * N + y] + 1
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                c = nx * N + ny
                if dist[c] < 0:
                    dist[c] = d
                    dq.append((nx, ny))
    return dist


def maxMoves(kx: int, ky: int, positions: List[List[int]]) -> int:
    n = len(positions)
    N = 50
    # Node n is the knight's starting position.
    pts = [tuple(p) for p in positions] + [(kx, ky)]
    D = []
    for (x, y) in pts:
        dist = _bfs(x, y)
        D.append([dist[px * N + py] for (px, py) in positions])
    full = (1 << n) - 1
    # dp[mask][i]: total remaining moves when pawns in mask are captured and
    # the knight stands on pawn i (i in mask).
    dp = [None] * (1 << n)
    dp[full] = [0] * n
    popc = [0] * (1 << n)
    for mask in range(1, 1 << n):
        popc[mask] = popc[mask >> 1] + (mask & 1)
    for mask in range(full - 1, 0, -1):
        rem = [j for j in range(n) if not (mask >> j) & 1]
        vals = [dp[mask | (1 << j)][j] for j in rem]
        alice = popc[mask] % 2 == 0
        row = [0] * n
        for i in range(n):
            if (mask >> i) & 1:
                Di = D[i]
                if alice:
                    row[i] = max(Di[j] + v for j, v in zip(rem, vals))
                else:
                    row[i] = min(Di[j] + v for j, v in zip(rem, vals))
        dp[mask] = row
    Dk = D[n]
    return max(Dk[j] + dp[1 << j][j] for j in range(n))
