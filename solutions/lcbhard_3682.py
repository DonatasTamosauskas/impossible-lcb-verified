MOD = 10**9 + 7


def countGoodArrays(n: int, m: int, k: int) -> int:
    a = n - 1
    num = 1
    den = 1
    for i in range(k):
        num = num * ((a - i) % MOD) % MOD
        den = den * (i + 1) % MOD
    comb = num * pow(den, MOD - 2, MOD) % MOD
    return comb * (m % MOD) % MOD * pow(m - 1, n - 1 - k, MOD) % MOD
