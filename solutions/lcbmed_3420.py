from typing import List


def occurrencesOfElement(nums: List[int], queries: List[int], x: int) -> List[int]:
    pos = [i for i, v in enumerate(nums) if v == x]
    m = len(pos)
    return [pos[q - 1] if q <= m else -1 for q in queries]
