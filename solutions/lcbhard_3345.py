from typing import List


def sumOfPower(nums: List[int], k: int) -> int:
    MOD = 10**9 + 7
    # dp[s] = sum over subsets S with sum s of 2^(#elements not in S processed so far)
    dp = [0] * (k + 1)
    dp[0] = 1
    for x in nums:
        new = [(2 * v) % MOD for v in dp]
        if x <= k:
            for s in range(x, k + 1):
                new[s] = (new[s] + dp[s - x]) % MOD
        dp = new
    return dp[k] % MOD
