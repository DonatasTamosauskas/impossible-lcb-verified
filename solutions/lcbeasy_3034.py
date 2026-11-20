from typing import List


def numberOfPoints(nums: List[List[int]]) -> int:
    pts = set()
    for a, b in nums:
        pts.update(range(a, b + 1))
    return len(pts)
