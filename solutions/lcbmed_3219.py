from typing import List


def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    n = len(nums)
    order = sorted(range(n), key=lambda i: nums[i])
    res = [0] * n
    s = 0
    while s < n:
        e = s + 1
        while e < n and nums[order[e]] - nums[order[e - 1]] <= limit:
            e += 1
        idxs = sorted(order[s:e])
        for t, i in enumerate(idxs):
            res[i] = nums[order[s + t]]
        s = e
    return res
