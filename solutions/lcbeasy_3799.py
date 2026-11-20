from typing import List
from itertools import permutations


def totalNumbers(digits: List[int]) -> int:
    s = set()
    for a, b, c in permutations(digits, 3):
        if a != 0 and c % 2 == 0:
            s.add(a * 100 + b * 10 + c)
    return len(s)
