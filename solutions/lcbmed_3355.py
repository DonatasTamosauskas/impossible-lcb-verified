from typing import List


def minimumLevels(possible: List[int]) -> int:
    v = [1 if x else -1 for x in possible]
    total = sum(v)
    pre = 0
    for i in range(len(v) - 1):
        pre += v[i]
        if pre > total - pre:
            return i + 1
    return -1
