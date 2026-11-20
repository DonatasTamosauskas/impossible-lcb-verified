from typing import List
from collections import Counter


def minOperations(nums: List[int]) -> int:
    r = 0
    for c in Counter(nums).values():
        if c == 1:
            return -1
        r += (c + 2) // 3
    return r
