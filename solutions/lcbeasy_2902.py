from typing import List


def maxSum(nums: List[int]) -> int:
    best = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if max(str(nums[i])) == max(str(nums[j])):
                best = max(best, nums[i] + nums[j])
    return best
