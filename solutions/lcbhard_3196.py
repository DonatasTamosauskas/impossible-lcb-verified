from typing import List


def maxFrequencyScore(nums: List[int], k: int) -> int:
    a = sorted(nums)
    n = len(a)
    pre = [0] * (n + 1)
    for i, v in enumerate(a):
        pre[i + 1] = pre[i] + v

    def cost(l: int, r: int) -> int:
        m = (l + r) // 2
        med = a[m]
        left = med * (m - l) - (pre[m] - pre[l])
        right = (pre[r + 1] - pre[m + 1]) - med * (r - m)
        return left + right

    best = 0
    l = 0
    for r in range(n):
        while cost(l, r) > k:
            l += 1
        if r - l + 1 > best:
            best = r - l + 1
    return best
