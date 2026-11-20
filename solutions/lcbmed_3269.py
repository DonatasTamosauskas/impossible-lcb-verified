from typing import List


def countMatchingSubarrays(nums: List[int], pattern: List[int]) -> int:
    m = len(pattern)
    cnt = 0
    for i in range(len(nums) - m):
        ok = True
        for k in range(m):
            a, b = nums[i + k], nums[i + k + 1]
            d = (b > a) - (b < a)
            if d != pattern[k]:
                ok = False
                break
        cnt += ok
    return cnt
