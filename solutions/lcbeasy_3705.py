from typing import List


def largestInteger(nums: List[int], k: int) -> int:
    cnt = {}
    for i in range(len(nums) - k + 1):
        for v in set(nums[i:i + k]):
            cnt[v] = cnt.get(v, 0) + 1
    c = [v for v, t in cnt.items() if t == 1]
    return max(c) if c else -1
