from typing import List


def maxFrequency(nums: List[int], k: int, numOperations: int) -> int:
    m = max(nums)
    size = m + 2 * k + 3
    off = k + 1
    freq = [0] * size
    for x in nums:
        freq[x + off] += 1
    pre = [0] * (size + 1)
    for i in range(size):
        pre[i + 1] = pre[i] + freq[i]
    best = 0
    for t in range(size):
        lo = max(0, t - k)
        hi = min(size - 1, t + k)
        c = pre[hi + 1] - pre[lo]
        f = freq[t]
        best = max(best, f + min(numOperations, c - f))
    return best
