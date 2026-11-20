from typing import List


def shiftDistance(s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
    INF = float('inf')
    d = [[INF] * 26 for _ in range(26)]
    for i in range(26):
        d[i][i] = 0
        j = (i + 1) % 26
        d[i][j] = min(d[i][j], nextCost[i])
        j = (i - 1) % 26
        d[i][j] = min(d[i][j], previousCost[i])
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return int(sum(d[ord(a) - 97][ord(b) - 97] for a, b in zip(s, t)))
