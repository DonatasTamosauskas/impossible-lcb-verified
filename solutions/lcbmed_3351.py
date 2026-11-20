from typing import List


def maximumHappinessSum(happiness: List[int], k: int) -> int:
    h = sorted(happiness, reverse=True)
    t = 0
    for i in range(k):
        v = h[i] - i
        if v <= 0:
            break
        t += v
    return t
