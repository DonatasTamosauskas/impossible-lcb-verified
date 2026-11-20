import heapq
from typing import List


def maxRemoval(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    qs = sorted(queries)
    j = 0
    avail = []
    ends = []
    used = 0
    for i in range(n):
        while j < len(qs) and qs[j][0] <= i:
            heapq.heappush(avail, -qs[j][1])
            j += 1
        while ends and ends[0] < i:
            heapq.heappop(ends)
        while nums[i] > len(ends):
            if not avail or -avail[0] < i:
                return -1
            heapq.heappush(ends, -heapq.heappop(avail))
            used += 1
    return len(queries) - used
