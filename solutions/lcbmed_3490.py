from typing import List


def maximumLength(nums: List[int]) -> int:
    ev = sum(1 for v in nums if v % 2 == 0)
    od = len(nums) - ev
    alt = 0
    last = -1
    for v in nums:
        p = v % 2
        if p != last:
            alt += 1
            last = p
    return max(ev, od, alt)
