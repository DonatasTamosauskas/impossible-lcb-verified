from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:
    best = None
    minpre = {}
    pre = 0
    for x in nums:
        if x not in minpre or pre < minpre[x]:
            minpre[x] = pre
        pre += x
        for v in (x - k, x + k):
            if v in minpre:
                s = pre - minpre[v]
                if best is None or s > best:
                    best = s
    return 0 if best is None else best
