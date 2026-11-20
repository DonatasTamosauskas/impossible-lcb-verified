from typing import List

MOD = 10**9 + 7


def numberOfPermutations(n: int, requirements: List[List[int]]) -> int:
    req = {}
    for e, c in requirements:
        req[e] = c
    M = max(req.values())  # inversion counts never exceed the final requirement (end n-1)
    # dp[j] = number of relative orderings of prefix with j inversions
    dp = [0] * (M + 1)
    dp[0] = 1
    if 0 in req:
        if req[0] != 0:
            return 0
    for i in range(1, n):
        # new element at position i can add k in [0, i] inversions
        pre = [0] * (M + 2)
        s = 0
        for j in range(M + 1):
            s = (s + dp[j]) % MOD
            pre[j + 1] = s
        ndp = [0] * (M + 1)
        for j in range(M + 1):
            lo = j - i
            if lo < 0:
                lo = 0
            ndp[j] = (pre[j + 1] - pre[lo]) % MOD
        if i in req:
            c = req[i]
            if c > M:
                return 0
            val = ndp[c]
            ndp = [0] * (M + 1)
            ndp[c] = val
        dp = ndp
    return sum(dp) % MOD
