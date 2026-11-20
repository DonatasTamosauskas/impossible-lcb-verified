from typing import List
from bisect import bisect_right


def gcdValues(nums: List[int], queries: List[int]) -> List[int]:
    M = max(nums)
    freq = [0] * (M + 1)
    for x in nums:
        freq[x] += 1
    exact = [0] * (M + 1)
    for d in range(M, 0, -1):
        c = 0
        for mult in range(d, M + 1, d):
            c += freq[mult]
        total = c * (c - 1) // 2
        for mult in range(2 * d, M + 1, d):
            total -= exact[mult]
        exact[d] = total
    prefix = [0] * (M + 1)
    run = 0
    for d in range(1, M + 1):
        run += exact[d]
        prefix[d] = run
    return [bisect_right(prefix, q) for q in queries]
