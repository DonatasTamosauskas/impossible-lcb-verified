MOD = 10**9 + 7


def numberOfWays(s: str, t: str, k: int) -> int:
    n = len(s)
    ss = s + s
    p0 = ss.find(t)
    if p0 == -1 or p0 >= n:
        return 0
    # smallest rotation period of s (divides n)
    per = ss.find(s, 1)
    if per == -1 or per > n:
        per = n
    cnt = n // per  # number of rotation offsets in [0, n) mapping s to t
    zero = 1 if p0 == 0 else 0
    inv_n = pow(n, MOD - 2, MOD)
    pw = pow(n - 1, k, MOD)
    sign = 1 if k % 2 == 0 else MOD - 1
    # ways to end at total shift 0 / at a specific nonzero shift after k moves
    f0 = (pw + (n - 1) * sign) % MOD * inv_n % MOD
    f1 = (pw - sign) % MOD * inv_n % MOD
    return (zero * f0 + (cnt - zero) * f1) % MOD
