from typing import List


def returnToBoundaryCount(nums: List[int]) -> int:
    p = 0
    c = 0
    for x in nums:
        p += x
        if p == 0:
            c += 1
    return c
