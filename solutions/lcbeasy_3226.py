from typing import List


def numberGame(nums: List[int]) -> List[int]:
    s = sorted(nums)
    res = []
    for i in range(0, len(s), 2):
        res.append(s[i + 1])
        res.append(s[i])
    return res
