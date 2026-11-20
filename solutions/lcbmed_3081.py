from typing import List
from collections import Counter


def minLengthAfterRemovals(nums: List[int]) -> int:
    n = len(nums)
    m = max(Counter(nums).values())
    if 2 * m > n:
        return 2 * m - n
    return n % 2
