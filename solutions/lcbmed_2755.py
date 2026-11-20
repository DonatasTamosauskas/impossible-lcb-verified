from typing import List


def minExtraChar(s: str, dictionary: List[str]) -> int:
    words = set(dictionary)
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i):
            if s[j:i] in words and dp[j] < dp[i]:
                dp[i] = dp[j]
    return dp[n]
