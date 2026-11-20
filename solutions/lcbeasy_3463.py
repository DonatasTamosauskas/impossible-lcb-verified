from typing import List


def numberOfAlternatingGroups(colors: List[int]) -> int:
    n = len(colors)
    return sum(
        1 for i in range(n)
        if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]
    )
