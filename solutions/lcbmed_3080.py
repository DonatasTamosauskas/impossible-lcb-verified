from typing import List


def maxSubarrays(nums: List[int]) -> int:
    t = nums[0]
    for v in nums:
        t &= v
    if t != 0:
        return 1
    cnt = 0
    cur = -1
    for v in nums:
        cur &= v
        if cur == 0:
            cnt += 1
            cur = -1
    return cnt
