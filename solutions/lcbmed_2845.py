from typing import List


def findValueOfPartition(nums: List[int]) -> int:
    s = sorted(nums)
    return min(s[i + 1] - s[i] for i in range(len(s) - 1))
