from typing import List
from collections import defaultdict


def maxSubarrayLength(nums: List[int], k: int) -> int:
    cnt = defaultdict(int)
    l = 0
    best = 0
    for r, v in enumerate(nums):
        cnt[v] += 1
        while cnt[v] > k:
            cnt[nums[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
