def minimumBeautifulSubstrings(s: str) -> int:
    pw = set()
    p = 1
    while p < (1 << 15):
        pw.add(bin(p)[2:])
        p *= 5
    n = len(s)
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] < INF and s[j:i] in pw:
                dp[i] = min(dp[i], dp[j] + 1)
    return dp[n] if dp[n] < INF else -1
