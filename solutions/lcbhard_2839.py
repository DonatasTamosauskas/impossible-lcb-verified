from bisect import bisect_left
from typing import List


def maximumSumQueries(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    pts = sorted(zip(nums1, nums2), key=lambda t: -t[0])
    order = sorted(range(len(queries)), key=lambda i: -queries[i][0])
    ans = [-1] * len(queries)
    ys: List[int] = []
    sums: List[int] = []
    p = 0
    m = len(pts)
    for qi in order:
        x, y = queries[qi][0], queries[qi][1]
        while p < m and pts[p][0] >= x:
            a, b = pts[p]
            p += 1
            s = a + b
            if ys and ys[-1] >= b:
                continue
            while sums and sums[-1] <= s:
                sums.pop()
                ys.pop()
            ys.append(b)
            sums.append(s)
        k = bisect_left(ys, y)
        if k < len(ys):
            ans[qi] = sums[k]
    return ans
