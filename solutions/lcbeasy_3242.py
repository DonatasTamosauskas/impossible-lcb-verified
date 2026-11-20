from typing import List
from collections import Counter


def maxFrequencyElements(nums: List[int]) -> int:
    c = Counter(nums)
    m = max(c.values())
    return sum(v for v in c.values() if v == m)
