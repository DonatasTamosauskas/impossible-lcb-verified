def minimumSubstringsInPartition(s: str) -> int:
    n = len(s)
    INF = 10 ** 9
    dp = [INF] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        cnt = [0] * 26
        distinct = 0
        mx = 0
        best = INF
        for j in range(i - 1, -1, -1):
            c = ord(s[j]) - 97
            if cnt[c] == 0:
                distinct += 1
            cnt[c] += 1
            if cnt[c] > mx:
                mx = cnt[c]
            if mx * distinct == i - j and dp[j] + 1 < best:
                best = dp[j] + 1
        dp[i] = best
    return dp[n]
