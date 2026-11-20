from typing import List


def canAliceWin(nums: List[int]) -> bool:
    a = sum(v for v in nums if v < 10)
    b = sum(v for v in nums if v >= 10)
    return a != b
