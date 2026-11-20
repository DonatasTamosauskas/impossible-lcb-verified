from typing import List


def getGoodIndices(variables: List[List[int]], target: int) -> List[int]:
    res = []
    for i, (a, b, c, m) in enumerate(variables):
        if pow(pow(a, b, 10), c, m) == target:
            res.append(i)
    return res
