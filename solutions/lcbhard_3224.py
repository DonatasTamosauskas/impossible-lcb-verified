from typing import List

MOD = 10**9 + 7


def numberOfSequence(n: int, sick: List[int]) -> int:
    gaps = []
    inner_pow = 0
    if sick[0] > 0:
        gaps.append(sick[0])
    if sick[-1] < n - 1:
        gaps.append(n - 1 - sick[-1])
    for a, b in zip(sick, sick[1:]):
        g = b - a - 1
        if g > 0:
            gaps.append(g)
            inner_pow += g - 1
    total = sum(gaps)
    fact = [1] * (total + 1)
    for i in range(1, total + 1):
        fact[i] = fact[i - 1] * i % MOD
    res = fact[total]
    for g in gaps:
        res = res * pow(fact[g], MOD - 2, MOD) % MOD
    res = res * pow(2, inner_pow, MOD) % MOD
    return res
