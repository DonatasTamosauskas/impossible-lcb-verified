from typing import List


def minCosts(cost: List[int]) -> List[int]:
    res = []
    m = float('inf')
    for c in cost:
        m = min(m, c)
        res.append(m)
    return res
