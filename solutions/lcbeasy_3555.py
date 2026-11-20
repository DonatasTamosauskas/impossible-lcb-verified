import heapq
from typing import List


def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    res = list(nums)
    h = [(v, i) for i, v in enumerate(res)]
    heapq.heapify(h)
    for _ in range(k):
        v, i = heapq.heappop(h)
        v *= multiplier
        res[i] = v
        heapq.heappush(h, (v, i))
    return res
