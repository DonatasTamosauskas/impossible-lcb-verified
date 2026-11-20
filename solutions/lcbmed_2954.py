from typing import List
from collections import defaultdict


def maxSum(nums: List[int], m: int, k: int) -> int:
    cnt = defaultdict(int)
    s = 0
    best = 0
    for i, v in enumerate(nums):
        cnt[v] += 1
        s += v
        if i >= k:
            u = nums[i - k]
            s -= u
            cnt[u] -= 1
            if cnt[u] == 0:
                del cnt[u]
        if i >= k - 1 and len(cnt) >= m and s > best:
            best = s
    return best
