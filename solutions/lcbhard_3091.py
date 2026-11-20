from collections import Counter
from itertools import accumulate
from typing import List

MOD = 10**9 + 7


def countSubMultisets(nums: List[int], l: int, r: int) -> int:
    cnt = Counter(nums)
    zeros = cnt.pop(0, 0)
    limit = r
    dp = [0] * (limit + 1)
    dp[0] = 1
    reach = 0  # largest sum reachable so far (capped at limit)
    for v, c in cnt.items():
        if v > limit:
            continue
        reach = min(limit, reach + v * c)
        new = dp[:]
        # new[s] = sum_{t=0..c} dp[s - t*v], computed per residue class
        for res in range(min(v, reach + 1)):
            seq = dp[res:reach + 1:v]
            pre = list(accumulate(seq))
            w = c + 1
            out = [
                (pre[i] - (pre[i - w] if i >= w else 0)) % MOD
                for i in range(len(pre))
            ]
            new[res:res + len(out) * v:v] = out
        dp = new
    total = sum(dp[l:r + 1]) % MOD
    return total * (zeros + 1) % MOD
