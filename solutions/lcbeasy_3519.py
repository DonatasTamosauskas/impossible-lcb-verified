from collections import Counter
from typing import List


def winningPlayerCount(n: int, pick: List[List[int]]) -> int:
    c = Counter((x, y) for x, y in pick)
    won = {x for (x, y), v in c.items() if v > x}
    return len(won)
