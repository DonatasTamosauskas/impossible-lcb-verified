from typing import List


def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    INF = float("inf")
    d = [[INF] * 26 for _ in range(26)]
    for i in range(26):
        d[i][i] = 0
    for o, c, w in zip(original, changed, cost):
        a, b = ord(o) - 97, ord(c) - 97
        if w < d[a][b]:
            d[a][b] = w
    for k in range(26):
        dk = d[k]
        for i in range(26):
            dik = d[i][k]
            if dik == INF:
                continue
            di = d[i]
            for j in range(26):
                if dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    total = 0
    for s, t in zip(source, target):
        v = d[ord(s) - 97][ord(t) - 97]
        if v == INF:
            return -1
        total += v
    return total
