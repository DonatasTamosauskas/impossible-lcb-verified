def minimumOperations(num: str) -> int:
    n = len(num)
    best = n - 1 if '0' in num else n
    for t in ("00", "25", "50", "75"):
        j = num.rfind(t[1])
        if j < 0:
            continue
        i = num.rfind(t[0], 0, j)
        if i >= 0:
            best = min(best, n - i - 2)
    return best
