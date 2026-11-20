from typing import List


def maxWeight(pizzas: List[int]) -> int:
    a = sorted(pizzas)
    days = len(a) // 4
    odd = (days + 1) // 2
    even = days // 2
    r = 0
    hi = len(a) - 1
    for _ in range(odd):
        r += a[hi]
        hi -= 1
    for _ in range(even):
        r += a[hi - 1]
        hi -= 2
    return r
