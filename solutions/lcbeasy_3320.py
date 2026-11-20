from typing import List


def maxOperations(nums: List[int]) -> int:
    target = nums[0] + nums[1]
    c = 0
    for i in range(0, len(nums) - 1, 2):
        if nums[i] + nums[i + 1] != target:
            break
        c += 1
    return c
