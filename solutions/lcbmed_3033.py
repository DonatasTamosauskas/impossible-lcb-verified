def minOperations(s1: str, s2: str, x: int) -> int:
    p = [i for i in range(len(s1)) if s1[i] != s2[i]]
    m = len(p)
    if m % 2:
        return -1
    # doubled costs: each diff either x-matched (cost x each) or chain-paired with next (2*distance)
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0
    for i in range(m):
        if dp[i] == INF:
            continue
        dp[i + 1] = min(dp[i + 1], dp[i] + x)
        if i + 1 < m:
            dp[i + 2] = min(dp[i + 2], dp[i] + 2 * (p[i + 1] - p[i]))
    return dp[m] // 2
