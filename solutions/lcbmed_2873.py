from typing import List


def findPrimePairs(n: int) -> List[List[int]]:
    if n < 4:
        return []
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [[x, n - x] for x in range(2, n // 2 + 1) if s[x] and s[n - x]]
