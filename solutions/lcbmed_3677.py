from typing import List


def maximumAmount(coins: List[List[int]]) -> int:
    NEG = -10**18
    n = len(coins[0])
    prev = None
    for i, row in enumerate(coins):
        cur = [None] * n
        for j in range(n):
            c = row[j]
            if i == 0 and j == 0:
                a0 = c
                a1 = max(c, 0) if c < 0 else c
                a2 = a1
                cur[0] = (a0, a1, a2)
                continue
            b0 = b1 = b2 = NEG
            if i > 0:
                p = prev[j]
                b0, b1, b2 = p
            if j > 0:
                q = cur[j - 1]
                if q[0] > b0: b0 = q[0]
                if q[1] > b1: b1 = q[1]
                if q[2] > b2: b2 = q[2]
            n0 = b0 + c
            n1 = b1 + c
            n2 = b2 + c
            if c < 0:
                if b0 > n1: n1 = b0
                if b1 > n2: n2 = b1
            cur[j] = (n0, n1, n2)
        prev = cur
    return max(prev[n - 1])
