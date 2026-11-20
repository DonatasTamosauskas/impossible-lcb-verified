from typing import List


def minimumSumSubarray(nums: List[int], l: int, r: int) -> int:
    n = len(nums)
    best = -1
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            ln = j - i + 1
            if ln > r:
                break
            if ln >= l and s > 0 and (best == -1 or s < best):
                best = s
    return best
