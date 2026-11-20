from typing import List
from bisect import bisect_right

MOD = 10**9 + 7


def sumOfPowers(nums: List[int], k: int) -> int:
    a = sorted(nums)
    n = len(a)
    diffs = sorted({a[j] - a[i] for i in range(n) for j in range(i + 1, n)})

    def count_at_least(d: int) -> int:
        # number of k-subsequences (of sorted a) whose adjacent gaps are all >= d
        lim = [min(i, bisect_right(a, a[i] - d)) for i in range(n)]
        cur = [1] * n  # length-1 subsequences ending at i
        for _ in range(k - 1):
            pre = [0] * (n + 1)
            s = 0
            for i in range(n):
                s += cur[i]
                pre[i + 1] = s % MOD
            cur = [pre[lim[i]] for i in range(n)]
        return sum(cur) % MOD

    f = [count_at_least(d) for d in diffs]
    f.append(0)
    ans = 0
    for i, d in enumerate(diffs):
        ans = (ans + d % MOD * ((f[i] - f[i + 1]) % MOD)) % MOD
    return ans
