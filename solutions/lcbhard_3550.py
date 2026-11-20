from typing import List


def _top3(colmax, n):
    # returns up to 3 (value, col) with distinct columns, highest values
    best = []
    for c in range(n):
        v = colmax[c]
        if v is None:
            continue
        if len(best) < 3:
            best.append((v, c))
            best.sort(reverse=True)
        elif v > best[-1][0]:
            best[-1] = (v, c)
            best.sort(reverse=True)
    return best


def maximumValueSum(board: List[List[int]]) -> int:
    m = len(board)
    n = len(board[0])
    NEG = None
    pre = [None] * m
    colmax = [NEG] * n
    for r in range(m):
        pre[r] = _top3(colmax, n)
        row = board[r]
        for c in range(n):
            if colmax[c] is None or row[c] > colmax[c]:
                colmax[c] = row[c]
    suf = [None] * m
    colmax = [NEG] * n
    for r in range(m - 1, -1, -1):
        suf[r] = _top3(colmax, n)
        row = board[r]
        for c in range(n):
            if colmax[c] is None or row[c] > colmax[c]:
                colmax[c] = row[c]

    best = None
    for r in range(1, m - 1):
        up = pre[r]
        down = suf[r]
        row = board[r]
        for c in range(n):
            v = row[c]
            for uv, uc in up:
                if uc == c:
                    continue
                for dv, dc in down:
                    if dc == c or dc == uc:
                        continue
                    t = v + uv + dv
                    if best is None or t > best:
                        best = t
                    break
    return best
