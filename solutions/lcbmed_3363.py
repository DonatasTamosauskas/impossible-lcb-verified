import heapq
from typing import List


def mostFrequentIDs(nums: List[int], freq: List[int]) -> List[int]:
    cnt = {}
    h = []
    ans = []
    for x, d in zip(nums, freq):
        c = cnt.get(x, 0) + d
        cnt[x] = c
        heapq.heappush(h, (-c, x))
        while h and cnt[h[0][1]] != -h[0][0]:
            heapq.heappop(h)
        ans.append(-h[0][0] if h else 0)
    return ans
