from typing import List


def minimumSubarrayLength(nums: List[int], k: int) -> int:
    n = len(nums)
    best = -1
    for i in range(n):
        o = 0
        for j in range(i, n):
            o |= nums[j]
            if o >= k:
                if best == -1 or j - i + 1 < best:
                    best = j - i + 1
                break
    return best
