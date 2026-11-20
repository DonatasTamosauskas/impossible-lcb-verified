from typing import List


def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    n = len(baskets)
    size = 1
    while size < n:
        size *= 2
    t = [0] * (2 * size)
    t[size:size + n] = baskets
    for i in range(size - 1, 0, -1):
        t[i] = max(t[2 * i], t[2 * i + 1])
    un = 0
    for f in fruits:
        if t[1] < f:
            un += 1
            continue
        i = 1
        while i < size:
            i = 2 * i if t[2 * i] >= f else 2 * i + 1
        t[i] = 0
        i >>= 1
        while i:
            t[i] = max(t[2 * i], t[2 * i + 1])
            i >>= 1
    return un
