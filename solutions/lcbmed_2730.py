from typing import List


def maximumOr(nums: List[int], k: int) -> int:
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] | nums[i]
    suf = 0
    best = 0
    for i in range(n - 1, -1, -1):
        best = max(best, pre[i] | (nums[i] << k) | suf)
        suf |= nums[i]
    return best
