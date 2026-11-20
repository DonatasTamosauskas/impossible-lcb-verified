from typing import List


def maxSum(nums: List[int], k: int, m: int) -> int:
    n = len(nums)
    NEG = float("-inf")
    P = [0] * (n + 1)
    for i, x in enumerate(nums):
        P[i + 1] = P[i] + x
    prev = [0] * (n + 1)
    for j in range(1, k + 1):
        cur = [NEG] * (n + 1)
        bestv = NEG
        for i in range(1, n + 1):
            t = i - m
            if t >= 0 and prev[t] != NEG:
                v = prev[t] - P[t]
                if v > bestv:
                    bestv = v
            c = cur[i - 1]
            if bestv != NEG and bestv + P[i] > c:
                c = bestv + P[i]
            cur[i] = c
        prev = cur
    return int(prev[n])
