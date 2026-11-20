from typing import List


def missingInteger(nums: List[int]) -> int:
    s = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            break
        s += nums[i]
    st = set(nums)
    while s in st:
        s += 1
    return s
