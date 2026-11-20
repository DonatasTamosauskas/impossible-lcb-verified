from typing import List


def maximumStrength(nums: List[int], k: int) -> int:
    n = len(nums)
    NEG = -(10 ** 40)
    prev = [0] * (n + 1)
    for j in range(1, k + 1):
        w = k - j + 1
        if j % 2 == 0:
            w = -w
        new = [NEG] * (n + 1)
        cur_end = NEG
        best = NEG
        for i in range(j - 1, n):
            p = prev[i]
            e = (cur_end if cur_end > p else p) + w * nums[i]
            cur_end = e
            if e > best:
                best = e
            new[i + 1] = best
        prev = new
    return prev[n]
