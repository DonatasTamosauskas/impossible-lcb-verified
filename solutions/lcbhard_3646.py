from typing import List


def sumOfGoodSubsequences(nums: List[int]) -> int:
    MOD = 10**9 + 7
    m = max(nums) + 2
    cnt = [0] * (m + 1)
    sm = [0] * (m + 1)
    for x in nums:
        c = 1 + cnt[x + 1]
        s = sm[x + 1]
        if x > 0:
            c += cnt[x - 1]
            s += sm[x - 1]
        c %= MOD
        s = (s + x * c) % MOD
        cnt[x] = (cnt[x] + c) % MOD
        sm[x] = (sm[x] + s) % MOD
    return sum(sm) % MOD
