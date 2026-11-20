from typing import List


def minimumOperations(nums: List[int], target: List[int]) -> int:
    ans = 0
    prev_p = 0
    prev_q = 0
    for a, b in zip(nums, target):
        d = b - a
        p = d if d > 0 else 0
        q = -d if d < 0 else 0
        if p > prev_p:
            ans += p - prev_p
        if q > prev_q:
            ans += q - prev_q
        prev_p, prev_q = p, q
    return ans
