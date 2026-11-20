from collections import deque
from typing import List


def findMaximumLength(nums: List[int]) -> int:
    n = len(nums)
    pre = [0] * (n + 1)
    for i, v in enumerate(nums):
        pre[i + 1] = pre[i] + v
    dp = [0] * (n + 1)
    last = [0] * (n + 1)
    # key[j] = pre[j] + last[j]; transition from the largest j with key[j] <= pre[i]
    dq = deque([0])
    for i in range(1, n + 1):
        p = pre[i]
        while len(dq) > 1 and pre[dq[1]] + last[dq[1]] <= p:
            dq.popleft()
        j = dq[0]
        dp[i] = dp[j] + 1
        last[i] = p - pre[j]
        key = p + last[i]
        while dq and pre[dq[-1]] + last[dq[-1]] >= key:
            dq.pop()
        dq.append(i)
    return dp[n]
