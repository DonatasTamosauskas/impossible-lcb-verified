from typing import List


def hasIncreasingSubarrays(nums: List[int], k: int) -> bool:
    def inc(s: int) -> bool:
        return all(nums[j] < nums[j + 1] for j in range(s, s + k - 1))

    return any(inc(a) and inc(a + k) for a in range(len(nums) - 2 * k + 1))
