from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    m = max(nums)
    pos = [i for i, v in enumerate(nums) if v == m]
    n = len(nums)
    res = 0
    for i in range(len(pos) - k + 1):
        left = pos[i] - (pos[i - 1] if i > 0 else -1)
        res += left * (n - pos[i + k - 1])
    return res
