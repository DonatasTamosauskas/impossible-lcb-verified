from typing import List


def constructTransformedArray(nums: List[int]) -> List[int]:
    n = len(nums)
    return [nums[(i + v) % n] for i, v in enumerate(nums)]
