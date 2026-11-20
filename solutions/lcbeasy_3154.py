from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    best = 0
    mx = nums[0]
    md = 0
    for x in nums[1:]:
        best = max(best, md * x)
        md = max(md, mx - x)
        mx = max(mx, x)
    return best
