from typing import List
from functools import cmp_to_key


def minDamage(power: int, damage: List[int], health: List[int]) -> int:
    n = len(damage)
    t = [(h + power - 1) // power for h in health]
    order = list(range(n))

    def cmp(i, j):
        a = t[i] * damage[j]
        b = t[j] * damage[i]
        return -1 if a < b else (1 if a > b else 0)

    order.sort(key=cmp_to_key(cmp))
    total = 0
    elapsed = 0
    for i in order:
        elapsed += t[i]
        total += elapsed * damage[i]
    return total
