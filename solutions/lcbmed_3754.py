def maxDistance(s: str, k: int) -> int:
    x = y = 0
    best = 0
    for i, c in enumerate(s, 1):
        if c == 'N':
            y += 1
        elif c == 'S':
            y -= 1
        elif c == 'E':
            x += 1
        else:
            x -= 1
        best = max(best, min(i, abs(x) + abs(y) + 2 * k))
    return best
