from typing import List


def minOperations(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)

    def cost(a_last, b_last, base):
        c = base
        for i in range(n - 1):
            x, y = nums1[i], nums2[i]
            if x <= a_last and y <= b_last:
                continue
            if y <= a_last and x <= b_last:
                c += 1
            else:
                return None
        return c

    res = []
    r = cost(nums1[-1], nums2[-1], 0)
    if r is not None:
        res.append(r)
    r = cost(nums2[-1], nums1[-1], 1)
    if r is not None:
        res.append(r)
    return min(res) if res else -1
