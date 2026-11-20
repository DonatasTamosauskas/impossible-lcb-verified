from typing import List


def minimumTime(nums1: List[int], nums2: List[int], x: int) -> int:
    n = len(nums1)
    pairs = sorted(zip(nums2, nums1))
    # dp[j] = maximum total reduction using j resets among processed items,
    # where the j-th reset (in nums2-ascending order) happens at second j.
    dp = [0] * (n + 1)
    for idx, (b, a) in enumerate(pairs):
        for j in range(idx + 1, 0, -1):
            cand = dp[j - 1] + a + b * j
            if cand > dp[j]:
                dp[j] = cand
    s1 = sum(nums1)
    s2 = sum(nums2)
    for t in range(n + 1):
        if s1 + s2 * t - dp[t] <= x:
            return t
    return -1
