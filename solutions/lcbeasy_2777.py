from typing import List


def distinctDifferenceArray(nums: List[int]) -> List[int]:
    n = len(nums)
    suf = [0] * (n + 1)
    seen = set()
    for i in range(n - 1, -1, -1):
        seen.add(nums[i])
        suf[i] = len(seen)
    seen = set()
    res = []
    for i in range(n):
        seen.add(nums[i])
        res.append(len(seen) - suf[i + 1])
    return res
