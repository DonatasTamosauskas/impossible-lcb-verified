from typing import List


def sumImbalanceNumbers(nums: List[int]) -> int:
    n = len(nums)
    size = max(nums) + 1
    total = 0
    for i in range(n):
        seen = [False] * (size + 2)
        segs = 0
        acc = 0
        for j in range(i, n):
            x = nums[j]
            if not seen[x]:
                seen[x] = True
                segs += 1 - seen[x - 1] - seen[x + 1]
            acc += segs - 1
        total += acc
    return total
