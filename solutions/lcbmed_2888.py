from typing import List


def minimumIndex(nums: List[int]) -> int:
    n = len(nums)
    from collections import Counter
    x, tot = Counter(nums).most_common(1)[0]
    c = 0
    for i in range(n - 1):
        if nums[i] == x:
            c += 1
        if c * 2 > i + 1 and (tot - c) * 2 > n - i - 1:
            return i
    return -1
