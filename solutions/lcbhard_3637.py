MOD = 10**9 + 7


def countBalancedPermutations(num: str) -> int:
    n = len(num)
    velunexorai = num
    cnt = [0] * 10
    for ch in velunexorai:
        cnt[ord(ch) - 48] += 1
    S = sum(d * cnt[d] for d in range(10))
    if S % 2:
        return 0
    half = S // 2
    E = (n + 1) // 2
    O = n // 2
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD
    # dp[j][s]: j digits placed on even positions with sum s, weighted by prod 1/(a!(c-a)!)
    dp = [[0] * (half + 1) for _ in range(E + 1)]
    dp[0][0] = 1
    for d in range(10):
        c = cnt[d]
        if c == 0:
            continue
        w = [inv[a] * inv[c - a] % MOD for a in range(c + 1)]
        ndp = [[0] * (half + 1) for _ in range(E + 1)]
        for j in range(E + 1):
            row = dp[j]
            for s in range(half + 1):
                v = row[s]
                if not v:
                    continue
                for a in range(c + 1):
                    nj = j + a
                    ns = s + a * d
                    if nj > E or ns > half:
                        break
                    ndp[nj][ns] = (ndp[nj][ns] + v * w[a]) % MOD
        dp = ndp
    return dp[E][half] * fact[E] % MOD * fact[O] % MOD
