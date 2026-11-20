from typing import List


def countCompleteSubarrays(nums: List[int]) -> int:
    k = len(set(nums))
    n = len(nums)
    cnt = {}
    res = 0
    l = 0
    for r, x in enumerate(nums):
        cnt[x] = cnt.get(x, 0) + 1
        while len(cnt) == k:
            res += n - r
            y = nums[l]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            l += 1
    return res
