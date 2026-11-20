def longestPalindromicSubsequence(s: str, k: int) -> int:
    n = len(s)
    K = k + 1
    zero = [0] * K
    prev = None  # dp[i+1][*]
    for i in range(n - 1, -1, -1):
        cur = [None] * n
        cur[i] = [1] * K
        for j in range(i + 1, n):
            v = list(map(max, prev[j], cur[j - 1]))
            d = abs(ord(s[i]) - ord(s[j]))
            d = min(d, 26 - d)
            if d <= k:
                inner = prev[j - 1] if i + 1 <= j - 1 else zero
                for c in range(d, K):
                    x = inner[c - d] + 2
                    if x > v[c]:
                        v[c] = x
            cur[j] = v
        prev = cur
    return prev[n - 1][k]
