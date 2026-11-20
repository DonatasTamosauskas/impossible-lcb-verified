from typing import List


def checkArray(nums: List[int], k: int) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)
    cur = 0
    for i in range(n):
        cur += diff[i]
        v = nums[i] - cur
        if v < 0:
            return False
        if v > 0:
            if i + k > n:
                return False
            cur += v
            diff[i + k] -= v
    return True
