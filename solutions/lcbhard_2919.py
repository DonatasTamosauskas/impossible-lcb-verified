from typing import List


def maxIncreasingGroups(usageLimits: List[int]) -> int:
    total = 0
    ans = 0
    for x in sorted(usageLimits):
        total += x
        if total >= (ans + 1) * (ans + 2) // 2:
            ans += 1
    return ans
