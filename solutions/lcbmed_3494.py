from typing import List


def minimumCost(m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
    items = [(c, 0) for c in horizontalCut] + [(c, 1) for c in verticalCut]
    items.sort(reverse=True)
    pieces = [1, 1]  # pieces[0]: horizontal segments count, pieces[1]: vertical
    total = 0
    for c, t in items:
        total += c * pieces[1 - t]
        pieces[t] += 1
    return total
