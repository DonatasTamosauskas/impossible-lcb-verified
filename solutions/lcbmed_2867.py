from typing import List


def numberOfGoodSubarraySplits(nums: List[int]) -> int:
    M = 10**9 + 7
    res = 1
    last = -1
    for i, x in enumerate(nums):
        if x == 1:
            if last >= 0:
                res = res * (i - last) % M
            last = i
    return res % M if last >= 0 else 0
