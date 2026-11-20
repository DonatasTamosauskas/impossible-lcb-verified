MOD = 10**9 + 7


def distanceSum(m: int, n: int, k: int) -> int:
    N = m * n
    # Sum of pairwise Manhattan distances over all unordered pairs of cells.
    row_part = (m - 1) * m * (m + 1) // 6 * n * n
    col_part = (n - 1) * n * (n + 1) // 6 * m * m
    total = (row_part + col_part) % MOD
    # Each pair of cells appears in C(N-2, k-2) arrangements.
    a = N - 2
    b = k - 2
    num = 1
    den = 1
    for i in range(b):
        num = num * ((a - i) % MOD) % MOD
        den = den * ((i + 1) % MOD) % MOD
    comb = num * pow(den, MOD - 2, MOD) % MOD
    return total * comb % MOD
