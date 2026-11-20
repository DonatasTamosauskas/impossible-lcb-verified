from typing import List


def specialPerm(nums: List[int]) -> int:
    n = len(nums)
    M = 10**9 + 7
    ok = [[nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0 for j in range(n)] for i in range(n)]
    dp = [[0] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 1
    for m in range(1, 1 << n):
        row = dp[m]
        for l in range(n):
            v = row[l]
            if not v:
                continue
            for j in range(n):
                if not (m >> j) & 1 and ok[l][j]:
                    nm = m | (1 << j)
                    dp[nm][j] = (dp[nm][j] + v) % M
    return sum(dp[(1 << n) - 1]) % M
