from typing import List


def resultsArray(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        ok = all(nums[j + 1] == nums[j] + 1 for j in range(i, i + k - 1))
        res.append(nums[i + k - 1] if ok else -1)
    return res
