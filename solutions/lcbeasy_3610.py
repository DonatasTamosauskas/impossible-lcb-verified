from collections import Counter
from typing import List


def findXSum(nums: List[int], k: int, x: int) -> List[int]:
    res = []
    for i in range(len(nums) - k + 1):
        cnt = Counter(nums[i:i + k])
        top = sorted(cnt.items(), key=lambda p: (-p[1], -p[0]))[:x]
        res.append(sum(v * c for v, c in top))
    return res
