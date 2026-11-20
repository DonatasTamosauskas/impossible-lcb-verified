from typing import List


def duplicateNumbersXOR(nums: List[int]) -> int:
    seen = set()
    res = 0
    for x in nums:
        if x in seen:
            res ^= x
        seen.add(x)
    return res
