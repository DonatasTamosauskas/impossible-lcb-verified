from typing import List


def minBitwiseArray(nums: List[int]) -> List[int]:
    res = []
    for n in nums:
        if n % 2 == 0:
            res.append(-1)
            continue
        t = 0
        while (n >> t) & 1:
            t += 1
        res.append(n - (1 << (t - 1)))
    return res
