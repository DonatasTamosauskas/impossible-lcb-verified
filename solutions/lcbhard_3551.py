from typing import List


def maximumSubarrayXor(nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    q = len(queries)
    # Group queries by subarray length.
    by_len = {}
    for idx, (l, r) in enumerate(queries):
        by_len.setdefault(r - l + 1, []).append((idx, l))
    ans = [0] * q
    f = list(nums)  # f[i] = XOR score of nums[i..i+L-1]
    m = list(nums)  # m[i] = max score over subarrays of nums[i..i+L-1]
    L = 1
    if L in by_len:
        for idx, l in by_len[L]:
            ans[idx] = m[l]
    for L in range(2, n + 1):
        f = [a ^ b for a, b in zip(f, f[1:])]
        m = [max(a, b, c) for a, b, c in zip(f, m, m[1:])]
        if L in by_len:
            for idx, l in by_len[L]:
                ans[idx] = m[l]
    return ans
