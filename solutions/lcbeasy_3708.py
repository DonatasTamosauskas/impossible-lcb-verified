from typing import List


def zigzagTraversal(grid: List[List[int]]) -> List[int]:
    seq = []
    for i, row in enumerate(grid):
        seq.extend(row if i % 2 == 0 else row[::-1])
    return seq[::2]
