def longestSemiRepetitiveSubstring(s: str) -> int:
    best = 1
    n = len(s)
    for i in range(n):
        pairs = 0
        for j in range(i + 1, n):
            if s[j] == s[j - 1]:
                pairs += 1
            if pairs > 1:
                break
            best = max(best, j - i + 1)
    return best
