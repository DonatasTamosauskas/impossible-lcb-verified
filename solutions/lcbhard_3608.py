from typing import List

MOD = 10**9 + 7


def subsequencePairCount(nums: List[int]) -> int:
    M = max(nums)
    freq = [0] * (M + 1)
    for v in nums:
        freq[v] += 1
    # cnt[d] = number of elements divisible by d
    cnt = [0] * (M + 1)
    for d in range(1, M + 1):
        cnt[d] = sum(freq[d::d])
    # Mobius function
    mu = [1] * (M + 1)
    is_comp = [False] * (M + 1)
    primes = []
    for i in range(2, M + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > M:
                break
            is_comp[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    n = len(nums)
    pow2 = [1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
    pow3 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow3[i] = pow3[i - 1] * 3 % MOD

    from math import gcd

    # f(a,b): ordered pairs of disjoint non-empty subsets, every element of S1 divisible by a,
    # every element of S2 divisible by b.
    def f(a, b):
        l = a // gcd(a, b) * b
        cl = cnt[l] if l <= M else 0
        ca, cb = cnt[a], cnt[b]
        return (pow3[cl] * pow2[ca + cb - 2 * cl] - pow2[ca] - pow2[cb] + 1) % MOD

    total = 0
    for g in range(1, M + 1):
        if cnt[g] < 2:
            continue
        mults = [a for a in range(g, M + 1, g) if mu[a // g] != 0 and cnt[a] > 0]
        for a in mults:
            ma = mu[a // g]
            for b in mults:
                total += ma * mu[b // g] * f(a, b)
        total %= MOD
    return total % MOD
