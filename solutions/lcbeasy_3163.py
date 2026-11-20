from typing import List


def sumCounts(nums: List[int]) -> int:
    total = 0
    for i in range(len(nums)):
        seen = set()
        for j in range(i, len(nums)):
            seen.add(nums[j])
            total += len(seen) ** 2
    return total
