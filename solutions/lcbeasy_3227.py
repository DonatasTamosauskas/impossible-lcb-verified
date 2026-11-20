from typing import List


def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    n2 = len(grid) ** 2
    seen = set()
    rep = 0
    for row in grid:
        for v in row:
            if v in seen:
                rep = v
            seen.add(v)
    miss = next(x for x in range(1, n2 + 1) if x not in seen)
    return [rep, miss]
