from itertools import permutations
from typing import List


def maxGoodNumber(nums: List[int]) -> int:
    return max(int("".join(bin(x)[2:] for x in p), 2) for p in permutations(nums))
