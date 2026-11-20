from typing import List


def maxSubarraySum(nums: List[int]) -> int:
    mx = max(nums)
    if mx <= 0:
        return mx
    INF = float("inf")
    f = {}
    pre = 0
    low = 0  # min plain prefix sum P[0..r-1]
    del_min = INF  # min over x of f[x]
    ans = -INF
    for v in nums:
        if v < 0:
            cur = f.get(v, INF)
            if low < cur:
                cur = low
            cur += v
            f[v] = cur
            if cur < del_min:
                del_min = cur
        pre += v
        m = low if low < del_min else del_min
        if pre - m > ans:
            ans = pre - m
        if pre < low:
            low = pre
    return int(ans)
