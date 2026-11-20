from typing import List


def minArraySum(nums: List[int], k: int, op1: int, op2: int) -> int:
    INF = 10**9
    dp = [[INF] * (op2 + 1) for _ in range(op1 + 1)]
    dp[0][0] = 0
    for x in nums:
        h = (x + 1) // 2
        c2 = x - k if x >= k else INF
        cb = INF
        if h >= k:
            cb = h - k
        if x >= k:
            cb = min(cb, (x - k + 1) // 2)
        for a in range(op1, -1, -1):
            row = dp[a]
            prow = dp[a - 1] if a else None
            for b in range(op2, -1, -1):
                best = row[b] + x
                if a:
                    v = prow[b] + h
                    if v < best:
                        best = v
                    if b and cb < INF:
                        v = prow[b - 1] + cb
                        if v < best:
                            best = v
                if b and c2 < INF:
                    v = row[b - 1] + c2
                    if v < best:
                        best = v
                row[b] = best
    return min(min(r) for r in dp)
