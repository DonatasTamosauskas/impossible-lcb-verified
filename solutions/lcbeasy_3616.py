from typing import List


def countValidSelections(nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for s in range(n):
        if nums[s] != 0:
            continue
        for d in (1, -1):
            a = nums[:]
            cur, dr = s, d
            while 0 <= cur < n:
                if a[cur] == 0:
                    cur += dr
                else:
                    a[cur] -= 1
                    dr = -dr
                    cur += dr
            if not any(a):
                count += 1
    return count
