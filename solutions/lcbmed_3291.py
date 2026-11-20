from typing import List


def canSortArray(nums: List[int]) -> bool:
    prev_max = 0
    i, n = 0, len(nums)
    while i < n:
        pc = bin(nums[i]).count("1")
        j = i
        mx, mn = 0, 10**9
        while j < n and bin(nums[j]).count("1") == pc:
            mx = max(mx, nums[j])
            mn = min(mn, nums[j])
            j += 1
        if mn < prev_max:
            return False
        prev_max = mx
        i = j
    return True
