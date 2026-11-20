MOD = 10**9 + 7


def numberOfWays(n: int, x: int, y: int) -> int:
    # dp[j] = ways to assign first i performers using exactly j distinct (labelled) stages
    k = min(n, x)
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        new = [0] * (k + 1)
        top = min(i, k)
        for j in range(1, top + 1):
            new[j] = (dp[j] * j + dp[j - 1] * (x - j + 1)) % MOD
        dp = new
    res = 0
    pw = 1
    for j in range(1, k + 1):
        pw = pw * y % MOD
        res = (res + dp[j] * pw) % MOD
    return res
