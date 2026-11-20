def minimumChairs(s: str) -> int:
    cur = best = 0
    for c in s:
        cur += 1 if c == 'E' else -1
        best = max(best, cur)
    return best
