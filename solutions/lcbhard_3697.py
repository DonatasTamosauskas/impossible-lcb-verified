from typing import List
from math import gcd
import heapq


def minimumIncrements(nums: List[int], target: List[int]) -> int:
    m = len(target)
    full = (1 << m) - 1
    lcms = [1] * (full + 1)
    for mask in range(1, full + 1):
        low = mask & (-mask)
        j = low.bit_length() - 1
        prev = lcms[mask ^ low]
        t = target[j]
        lcms[mask] = prev // gcd(prev, t) * t
    # For each mask, only the m cheapest nums can matter
    cand = set()
    for mask in range(1, full + 1):
        L = lcms[mask]
        best = heapq.nsmallest(m, range(len(nums)), key=lambda i: (-nums[i]) % L)
        cand.update(best)
    INF = float('inf')
    dp = [INF] * (full + 1)
    dp[0] = 0
    for i in cand:
        x = nums[i]
        cost = [0] * (full + 1)
        for mask in range(1, full + 1):
            cost[mask] = (-x) % lcms[mask]
        ndp = dp[:]
        for mask in range(full + 1):
            if dp[mask] == INF:
                continue
            rest = full ^ mask
            sub = rest
            while sub:
                nm = mask | sub
                v = dp[mask] + cost[sub]
                if v < ndp[nm]:
                    ndp[nm] = v
                sub = (sub - 1) & rest
        dp = ndp
    return int(dp[full])
