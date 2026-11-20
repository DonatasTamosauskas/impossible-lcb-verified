from typing import List


def maximumSetSize(nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = set(nums1), set(nums2)
    h = len(nums1) // 2
    return min(len(s1 | s2), min(len(s1), h) + min(len(s2), h))
