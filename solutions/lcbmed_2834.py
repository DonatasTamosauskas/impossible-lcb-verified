from typing import List


def relocateMarbles(nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
    occ = set(nums)
    for a, b in zip(moveFrom, moveTo):
        if a != b:
            occ.discard(a)
            occ.add(b)
    return sorted(occ)
