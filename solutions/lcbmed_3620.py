from typing import List


def maxDistinctElements(nums: List[int], k: int) -> int:
    cur = None
    cnt = 0
    for x in sorted(nums):
        v = x - k
        if cur is not None and cur + 1 > v:
            v = cur + 1
        if v <= x + k:
            cnt += 1
            cur = v
    return cnt
