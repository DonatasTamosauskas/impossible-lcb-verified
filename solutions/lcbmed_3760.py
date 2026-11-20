from typing import List


def assignElements(groups: List[int], elements: List[int]) -> List[int]:
    M = max(groups)
    best = [-1] * (M + 1)
    seen = set()
    for j, v in enumerate(elements):
        if v in seen or v > M:
            continue
        seen.add(v)
        for m in range(v, M + 1, v):
            if best[m] == -1:
                best[m] = j
    return [best[g] for g in groups]
