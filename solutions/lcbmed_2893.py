from typing import List


def maxScore(nums: List[int], x: int) -> int:
    NEG = float("-inf")
    best = [NEG, NEG]
    best[nums[0] & 1] = nums[0]
    for v in nums[1:]:
        p = v & 1
        cur = max(best[p], best[1 - p] - x) + v
        best[p] = max(best[p], cur)
    return int(max(best))
