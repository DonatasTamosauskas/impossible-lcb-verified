from typing import List


def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)

    def ok(k):
        bits = [1] * n
        for l, r, v in queries[:k]:
            for i in range(l, r + 1):
                bits[i] |= bits[i] << v
        return all((bits[i] >> nums[i]) & 1 for i in range(n))

    if not ok(len(queries)):
        return -1
    lo, hi = 0, len(queries)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
