from typing import List


def minCost(nums: List[int], x: int) -> int:
    n = len(nums)
    cur = list(nums)
    best = sum(cur)
    for k in range(1, n):
        for i in range(n):
            j = nums[(i - k) % n]
            if j < cur[i]:
                cur[i] = j
        best = min(best, sum(cur) + k * x)
    return best
