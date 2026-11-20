from typing import List


def matrixSum(nums: List[List[int]]) -> int:
    rows = [sorted(r) for r in nums]
    return sum(max(c) for c in zip(*[r for r in rows]) ) if len({len(r) for r in rows}) == 1 else _slow(rows)


def _slow(rows):
    total = 0
    rows = [sorted(r) for r in rows]
    while any(rows):
        total += max(r.pop() for r in rows if r)
    return total
