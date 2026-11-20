from typing import List


def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    s1, s2 = set(nums1), set(nums2)
    return [sum(1 for v in nums1 if v in s2), sum(1 for v in nums2 if v in s1)]
