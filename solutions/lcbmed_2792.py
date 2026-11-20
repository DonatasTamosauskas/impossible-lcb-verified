from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:
    x = 0
    for d in derived:
        x ^= d
    return x == 0
