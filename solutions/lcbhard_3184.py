from typing import List


def maxBalancedSubsequenceSum(nums: List[int]) -> int:
    n = len(nums)
    keys = [nums[i] - i for i in range(n)]
    sorted_keys = sorted(set(keys))
    rank = {v: i + 1 for i, v in enumerate(sorted_keys)}
    size = len(sorted_keys)
    NEG = float("-inf")
    tree = [NEG] * (size + 1)
    best = max(nums)
    for i in range(n):
        r = rank[keys[i]]
        q = NEG
        j = r
        while j > 0:
            if tree[j] > q:
                q = tree[j]
            j -= j & -j
        cur = nums[i] + (q if q > 0 else 0)
        if cur > best:
            best = cur
        j = r
        while j <= size:
            if tree[j] < cur:
                tree[j] = cur
            j += j & -j
    return int(best)
