from typing import List


def sumDigitDifferences(nums: List[int]) -> int:
    n = len(nums)
    total = 0
    strs = [str(x) for x in nums]
    for col in zip(*strs):
        cnt = {}
        for ch in col:
            cnt[ch] = cnt.get(ch, 0) + 1
        same = sum(c * (c - 1) // 2 for c in cnt.values())
        total += n * (n - 1) // 2 - same
    return total
