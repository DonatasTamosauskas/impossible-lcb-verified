from typing import List


def countOfPairs(nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    # dp[v]: number of ways with arr1[i] == v
    dp = [1] * (nums[0] + 1)
    for i in range(1, n):
        prev = dp
        a, b = nums[i - 1], nums[i]
        d = max(0, b - a)
        pre = [0] * (a + 1)
        s = 0
        for v in range(a + 1):
            s = (s + prev[v]) % MOD
            pre[v] = s
        cur = [0] * (b + 1)
        for v in range(b + 1):
            lim = min(v - d, a)
            if lim >= 0:
                cur[v] = pre[lim]
        dp = cur
    return sum(dp) % MOD
