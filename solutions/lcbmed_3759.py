import heapq
from typing import List


def findMaxSum(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    n = len(nums1)
    order = sorted(range(n), key=lambda i: nums1[i])
    ans = [0] * n
    heap = []
    total = 0
    i = 0
    while i < n:
        j = i
        while j < n and nums1[order[j]] == nums1[order[i]]:
            ans[order[j]] = total
            j += 1
        for t in range(i, j):
            v = nums2[order[t]]
            if len(heap) < k:
                heapq.heappush(heap, v)
                total += v
            elif v > heap[0]:
                total += v - heapq.heapreplace(heap, v)
        i = j
    return ans
