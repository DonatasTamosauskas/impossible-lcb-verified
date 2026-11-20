from typing import List


def incremovableSubarrayCount(nums: List[int]) -> int:
    n = len(nums)

    def inc(a):
        return all(a[i] < a[i + 1] for i in range(len(a) - 1))

    return sum(
        1
        for i in range(n)
        for j in range(i, n)
        if inc(nums[:i] + nums[j + 1:])
    )
