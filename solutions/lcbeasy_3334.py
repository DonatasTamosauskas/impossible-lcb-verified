from typing import List


def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    need = sum(apple)
    c = 0
    for cap in sorted(capacity, reverse=True):
        if need <= 0:
            break
        need -= cap
        c += 1
    return c
