from typing import List


def minSizeSubarray(nums: List[int], target: int) -> int:
    n = len(nums)
    tot = sum(nums)
    q, r = divmod(target, tot)
    if r == 0:
        return q * n
    best = None
    left = 0
    cur = 0
    b = nums + nums
    for right in range(2 * n):
        cur += b[right]
        while cur > r and left <= right:
            cur -= b[left]
            left += 1
        if cur == r:
            L = right - left + 1
            if best is None or L < best:
                best = L
    if best is None:
        return -1
    return q * n + best
