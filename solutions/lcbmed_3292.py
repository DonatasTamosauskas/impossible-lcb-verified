from typing import List


def earliestSecondToMarkIndices(nums: List[int], changeIndices: List[int]) -> int:
    n, m = len(nums), len(changeIndices)

    def ok(s):
        last = {}
        for t in range(s):
            last[changeIndices[t] - 1] = t
        if len(last) < n:
            return False
        lastset = {t: i for i, t in last.items()}
        free = 0
        for t in range(s):
            if t in lastset:
                need = nums[lastset[t]]
                if free < need:
                    return False
                free -= need
            else:
                free += 1
        return True

    if not ok(m):
        return -1
    lo, hi = 1, m
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
