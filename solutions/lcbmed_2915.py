from typing import List
from collections import defaultdict


def countInterestingSubarrays(nums: List[int], modulo: int, k: int) -> int:
    cnt = defaultdict(int)
    cnt[0] = 1
    p = 0
    ans = 0
    for v in nums:
        if v % modulo == k:
            p = (p + 1) % modulo
        ans += cnt[(p - k) % modulo]
        cnt[p] += 1
    return ans
