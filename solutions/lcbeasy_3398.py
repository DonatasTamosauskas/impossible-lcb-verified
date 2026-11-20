from typing import List


def canMakeSquare(grid: List[List[str]]) -> bool:
    for i in range(2):
        for j in range(2):
            b = sum(grid[i + a][j + c] == 'B' for a in range(2) for c in range(2))
            if b != 2:
                return True
    return False
