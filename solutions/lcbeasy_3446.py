from typing import List


def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
    return sum(1 for a in nums1 for b in nums2 if a % (b * k) == 0)
