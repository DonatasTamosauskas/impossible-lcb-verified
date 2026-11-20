from typing import List


def countAlternatingSubarrays(nums: List[int]) -> int:
    total = 0
    run = 0
    prev = None
    for x in nums:
        run = run + 1 if prev is not None and x != prev else 1
        total += run
        prev = x
    return total
