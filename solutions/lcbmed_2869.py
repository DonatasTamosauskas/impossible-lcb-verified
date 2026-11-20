from typing import List


def maxNonDecreasingLength(nums1: List[int], nums2: List[int]) -> int:
    a = b = 1
    best = 1
    for i in range(1, len(nums1)):
        na = nb = 1
        for pv, pl in ((nums1[i-1], a), (nums2[i-1], b)):
            if pv <= nums1[i]:
                na = max(na, pl + 1)
            if pv <= nums2[i]:
                nb = max(nb, pl + 1)
        a, b = na, nb
        best = max(best, a, b)
    return best
