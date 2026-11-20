def numberOfWays(n: int, x: int) -> int:
    M = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    i = 1
    while i ** x <= n:
        p = i ** x
        for s in range(n, p - 1, -1):
            dp[s] = (dp[s] + dp[s - p]) % M
        i += 1
    return dp[n]
