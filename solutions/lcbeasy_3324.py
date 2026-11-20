from typing import List
from collections import Counter


def isPossibleToSplit(nums: List[int]) -> bool:
    return max(Counter(nums).values()) <= 2
