def stringCount(n: int) -> int:
    M = 10**9 + 7
    p = lambda b, e: pow(b, e, M)
    total = p(26, n)
    no_l = p(25, n)
    no_t = p(25, n)
    e_lt2 = (p(25, n) + n * p(25, n - 1)) % M
    l_t = p(24, n)
    l_e = (p(24, n) + n * p(24, n - 1)) % M
    all3 = (p(23, n) + n * p(23, n - 1)) % M
    return (total - no_l - no_t - e_lt2 + l_t + 2 * l_e - all3) % M
