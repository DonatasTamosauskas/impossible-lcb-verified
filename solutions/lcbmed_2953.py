from typing import List
from collections import defaultdict


def countPairs(coordinates: List[List[int]], k: int) -> int:
    seen = defaultdict(int)
    ans = 0
    for x, y in coordinates:
        for i in range(k + 1):
            ans += seen.get((x ^ i, y ^ (k - i)), 0)
        seen[(x, y)] += 1
    return ans
