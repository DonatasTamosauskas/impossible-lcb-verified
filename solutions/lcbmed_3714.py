from typing import List

MOD = 10**9 + 7


def minMaxSums(nums: List[int], k: int) -> int:
    n = len(nums)
    a = sorted(nums)
    N = n + 1
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def C(m, t):
        if t < 0 or t > m:
            return 0
        return fact[m] * inv[t] % MOD * inv[m - t] % MOD

    # S[m] = sum_{t=0}^{k-1} C(m, t)
    S = [0] * (n + 1)
    S[0] = 1
    for m in range(n):
        S[m + 1] = (2 * S[m] - C(m, k - 1)) % MOD
    ans = 0
    for i in range(n):
        ans += a[i] * (S[i] + S[n - 1 - i])
    return ans % MOD
