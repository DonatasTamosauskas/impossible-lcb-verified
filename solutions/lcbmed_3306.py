import heapq
from typing import List


def unmarkedSumArray(nums: List[int], queries: List[List[int]]) -> List[int]:
    marked = [False] * len(nums)
    total = sum(nums)
    h = [(v, i) for i, v in enumerate(nums)]
    heapq.heapify(h)
    res = []
    for idx, k in queries:
        if not marked[idx]:
            marked[idx] = True
            total -= nums[idx]
        while k > 0 and h:
            v, i = heapq.heappop(h)
            if marked[i]:
                continue
            marked[i] = True
            total -= v
            k -= 1
        res.append(total)
    return res
