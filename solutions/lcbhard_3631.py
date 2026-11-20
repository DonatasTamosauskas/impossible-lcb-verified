MOD = 10**9 + 7


def countKReducibleNumbers(s: str, k: int) -> int:
    L = len(s)
    # ops[c] = number of operations to reduce c to 1
    ops = [0] * (L + 1)
    for c in range(2, L + 1):
        ops[c] = 1 + ops[bin(c).count("1")]
    good = [c >= 1 and ops[c] <= k - 1 for c in range(L + 1)]
    # binomials mod
    C = [[0] * (L + 1) for _ in range(L + 1)]
    for i in range(L + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    ans = 0
    ones = 0
    for i, ch in enumerate(s):
        if ch == "1":
            rem = L - i - 1
            row = C[rem]
            for t in range(rem + 1):
                if good[ones + t]:
                    ans += row[t]
            ans %= MOD
            ones += 1
    return ans % MOD
