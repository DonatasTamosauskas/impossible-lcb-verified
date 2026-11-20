from typing import List
from collections import deque


def continuousSubarrays(nums: List[int]) -> int:
    mx = deque()
    mn = deque()
    l = 0
    res = 0
    for r, x in enumerate(nums):
        while mx and nums[mx[-1]] <= x:
            mx.pop()
        mx.append(r)
        while mn and nums[mn[-1]] >= x:
            mn.pop()
        mn.append(r)
        while nums[mx[0]] - nums[mn[0]] > 2:
            l += 1
            if mx[0] < l:
                mx.popleft()
            if mn[0] < l:
                mn.popleft()
        res += r - l + 1
    return res
