from typing import List


def minimumArrayLength(nums: List[int]) -> int:
    m = min(nums)
    if any(v % m for v in nums):
        return 1
    return (nums.count(m) + 1) // 2
